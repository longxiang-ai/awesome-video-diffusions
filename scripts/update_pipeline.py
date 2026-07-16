import datetime
import json
import os
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

from arxiv_crawler import ArxivCrawler, ArxivFetchError
from paper_data import (
    PaperValidationError,
    build_archive_from_snapshots,
    find_latest_valid_snapshot,
    load_papers_file,
    merge_paper_collections,
    normalized_arxiv_id,
    validate_papers,
)
from readme_generator import ReadmeGenerator
from utils.logger import setup_logger


@dataclass(frozen=True)
class UpdateReport:
    status: str
    paper_count: int
    data_file: Optional[str]
    latest_data_date: Optional[str]
    stale_days: Optional[int]
    message: str

    def to_dict(self):
        return asdict(self)


class UpdatePipeline:
    def __init__(
        self,
        project_root: Path = Path("."),
        crawler_factory: Callable[[], ArxivCrawler] = ArxivCrawler,
        readme_factory: Optional[Callable[[], ReadmeGenerator]] = None,
        now_fn: Callable[[], datetime.datetime] = lambda: datetime.datetime.now(
            datetime.timezone.utc
        ),
        stale_grace_days: int = 3,
    ):
        self.project_root = Path(project_root).resolve()
        self.data_dir = self.project_root / "data"
        self.readme_path = self.project_root / "README.md"
        self.archive_path = self.data_dir / "paper_archive.json"
        self.crawler_factory = crawler_factory
        self.readme_factory = readme_factory
        self.now_fn = now_fn
        self.stale_grace_days = stale_grace_days
        self.logger = setup_logger("update_pipeline")

    def _relative_path(self, path: Path) -> str:
        try:
            return str(path.resolve().relative_to(self.project_root))
        except ValueError:
            return str(path)

    def _readme_generator(self) -> ReadmeGenerator:
        if self.readme_factory is not None:
            return self.readme_factory()
        return ReadmeGenerator(
            data_dir=self.data_dir,
            template_path=self.project_root / "README_template.md",
            readme_path=self.readme_path,
        )

    @staticmethod
    def _restore_file(path: Path, content: Optional[bytes]) -> None:
        if content is None:
            path.unlink(missing_ok=True)
        else:
            path.write_bytes(content)

    def _publish(
        self, replacements: Sequence[Tuple[Path, Path]]
    ) -> None:
        previous_contents = {
            target: target.read_bytes() if target.exists() else None
            for _, target in replacements
        }
        try:
            for temporary_path, target_path in replacements:
                os.replace(temporary_path, target_path)
        except Exception:
            for target_path, content in previous_contents.items():
                self._restore_file(target_path, content)
            raise

    def _load_archive(self) -> List[Dict[str, Any]]:
        if self.archive_path.exists():
            return load_papers_file(self.archive_path)
        return build_archive_from_snapshots(self.data_dir)

    def _fallback_report(
        self, today: datetime.date, error: BaseException
    ) -> UpdateReport:
        snapshot = find_latest_valid_snapshot(self.data_dir)
        if snapshot is None:
            return UpdateReport(
                status="failed",
                paper_count=0,
                data_file=None,
                latest_data_date=None,
                stale_days=None,
                message=f"Update failed and no valid historical snapshot exists: {error}",
            )

        stale_days = max(0, (today - snapshot.date).days)
        status = "degraded" if stale_days <= self.stale_grace_days else "failed"
        if status == "degraded":
            message = (
                f"arXiv update failed; preserving {snapshot.path.name} "
                f"({stale_days} day(s) old): {error}"
            )
        else:
            message = (
                f"arXiv update failed and latest valid snapshot "
                f"{snapshot.path.name} is {stale_days} day(s) old: {error}"
            )
        return UpdateReport(
            status=status,
            paper_count=len(snapshot.papers),
            data_file=self._relative_path(snapshot.path),
            latest_data_date=snapshot.date.isoformat(),
            stale_days=stale_days,
            message=message,
        )

    @staticmethod
    def write_report(report: UpdateReport, report_path: Path) -> None:
        report_path = Path(report_path)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = report_path.with_name(f".{report_path.name}.tmp")
        try:
            with temporary_path.open("w", encoding="utf-8") as handle:
                json.dump(report.to_dict(), handle, ensure_ascii=False, indent=2)
                handle.write("\n")
            os.replace(temporary_path, report_path)
        finally:
            temporary_path.unlink(missing_ok=True)

    def run(self, report_path: Path, max_results: Optional[int] = None) -> UpdateReport:
        now = self.now_fn()
        if now.tzinfo is None:
            now = now.replace(tzinfo=datetime.timezone.utc)
        now = now.astimezone(datetime.timezone.utc)
        today = now.date()

        try:
            latest_snapshot = find_latest_valid_snapshot(self.data_dir)
            crawler = self.crawler_factory()
            papers = crawler.search_papers(max_results=max_results)
            paper_dicts = validate_papers(papers)

            catchup_papers = []
            if latest_snapshot is not None:
                if latest_snapshot.date > today:
                    raise ArxivFetchError(
                        f"Latest snapshot date {latest_snapshot.date} is in the future"
                    )
                catchup_papers = crawler.search_papers_between(
                    latest_snapshot.date,
                    today,
                )

            existing_archive = self._load_archive()
            existing_ids = {
                normalized_arxiv_id(paper["arxiv_url"])
                for paper in existing_archive
            }
            archive_papers = merge_paper_collections(
                existing_archive,
                catchup_papers,
                paper_dicts,
            )
            added_to_archive = sum(
                normalized_arxiv_id(paper["arxiv_url"]) not in existing_ids
                for paper in archive_papers
            )
            data_path = self.data_dir / f"papers_{today.isoformat()}.json"

            with tempfile.TemporaryDirectory(
                prefix=".paper-update-", dir=self.project_root
            ) as temporary_dir:
                temporary_dir_path = Path(temporary_dir)
                temporary_data = temporary_dir_path / data_path.name
                temporary_archive = temporary_dir_path / self.archive_path.name
                temporary_readme = temporary_dir_path / "README.md"

                crawler.save_papers(papers, output_file=temporary_data)
                load_papers_file(temporary_data)
                crawler.save_papers(archive_papers, output_file=temporary_archive)
                load_papers_file(temporary_archive)
                generator = self._readme_generator()
                generator.generate_readme(
                    input_path=temporary_archive,
                    output_path=temporary_readme,
                    updated_at=now.replace(tzinfo=None),
                )
                if temporary_readme.stat().st_size == 0:
                    raise RuntimeError("Rendered README is empty")
                self._publish(
                    [
                        (temporary_data, data_path),
                        (temporary_archive, self.archive_path),
                        (temporary_readme, self.readme_path),
                    ]
                )

            report = UpdateReport(
                status="updated",
                paper_count=len(paper_dicts),
                data_file=self._relative_path(data_path),
                latest_data_date=today.isoformat(),
                stale_days=0,
                message=(
                    f"Published {len(paper_dicts)} latest papers; "
                    f"archive contains {len(archive_papers)} papers "
                    f"({added_to_archive} newly archived, "
                    f"{len(catchup_papers)} checked in catch-up range)"
                ),
            )
        except (ArxivFetchError, PaperValidationError) as exc:
            report = self._fallback_report(today, exc)
            annotation = "warning" if report.status == "degraded" else "error"
            if os.getenv("GITHUB_ACTIONS") == "true":
                print(f"::{annotation} title=Paper update {report.status}::{report.message}")
        except Exception as exc:
            report = UpdateReport(
                status="failed",
                paper_count=0,
                data_file=None,
                latest_data_date=None,
                stale_days=None,
                message=f"Update pipeline failed before publication: {exc}",
            )
            if os.getenv("GITHUB_ACTIONS") == "true":
                print(f"::error title=Paper update failed::{report.message}")

        self.write_report(report, report_path)
        self.logger.info("Update status: %s - %s", report.status, report.message)
        return report
