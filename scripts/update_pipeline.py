import datetime
import json
import os
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Optional

from arxiv_crawler import ArxivCrawler, ArxivFetchError, ArxivTemporaryError
from paper_data import (
    PaperValidationError,
    find_latest_valid_snapshot,
    load_papers_file,
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
    ):
        self.project_root = Path(project_root).resolve()
        self.data_dir = self.project_root / "data"
        self.readme_path = self.project_root / "README.md"
        self.crawler_factory = crawler_factory
        self.readme_factory = readme_factory
        self.now_fn = now_fn
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

    def _publish(self, temporary_data: Path, data_path: Path,
                 temporary_readme: Path) -> None:
        previous_data = data_path.read_bytes() if data_path.exists() else None
        previous_readme = self.readme_path.read_bytes() if self.readme_path.exists() else None
        try:
            os.replace(temporary_data, data_path)
            os.replace(temporary_readme, self.readme_path)
        except Exception:
            self._restore_file(data_path, previous_data)
            self._restore_file(self.readme_path, previous_readme)
            raise

    def _preserved_report(
        self, today: datetime.date, status: str, reason: str
    ) -> UpdateReport:
        snapshot = find_latest_valid_snapshot(self.data_dir)
        if snapshot is None:
            return UpdateReport(
                status="failed",
                paper_count=0,
                data_file=None,
                latest_data_date=None,
                stale_days=None,
                message=(
                    f"Cannot preserve paper data because no valid historical "
                    f"snapshot exists: {reason}"
                ),
            )

        stale_days = max(0, (today - snapshot.date).days)
        return UpdateReport(
            status=status,
            paper_count=len(snapshot.papers),
            data_file=self._relative_path(snapshot.path),
            latest_data_date=snapshot.date.isoformat(),
            stale_days=stale_days,
            message=(
                f"Preserving {snapshot.path.name} ({stale_days} day(s) old); "
                f"README and commit were skipped: {reason}"
            ),
        )

    def _failed_report(self, message: str) -> UpdateReport:
        return UpdateReport(
            status="failed",
            paper_count=0,
            data_file=None,
            latest_data_date=None,
            stale_days=None,
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
            crawler = self.crawler_factory()
            papers = crawler.search_papers(max_results=max_results)
            if not papers:
                report = self._preserved_report(
                    today,
                    "no_results",
                    "arXiv returned no relevant matching papers",
                )
                if os.getenv("GITHUB_ACTIONS") == "true":
                    annotation = "warning" if report.status != "failed" else "error"
                    print(
                        f"::{annotation} title=Paper update {report.status}::"
                        f"{report.message}"
                    )
                self.write_report(report, report_path)
                return report
            paper_dicts = validate_papers(papers)
            data_path = self.data_dir / f"papers_{today.isoformat()}.json"

            with tempfile.TemporaryDirectory(
                prefix=".paper-update-", dir=self.project_root
            ) as temporary_dir:
                temporary_dir_path = Path(temporary_dir)
                temporary_data = temporary_dir_path / data_path.name
                temporary_readme = temporary_dir_path / "README.md"

                crawler.save_papers(papers, output_file=temporary_data)
                load_papers_file(temporary_data)
                generator = self._readme_generator()
                generator.generate_readme(
                    input_path=temporary_data,
                    output_path=temporary_readme,
                    updated_at=now.replace(tzinfo=None),
                )
                if temporary_readme.stat().st_size == 0:
                    raise RuntimeError("Rendered README is empty")
                self._publish(temporary_data, data_path, temporary_readme)

            report = UpdateReport(
                status="updated",
                paper_count=len(paper_dicts),
                data_file=self._relative_path(data_path),
                latest_data_date=today.isoformat(),
                stale_days=0,
                message=f"Published {len(paper_dicts)} papers from arXiv",
            )
        except ArxivTemporaryError as exc:
            report = self._preserved_report(
                today, "temporary_failure", str(exc)
            )
            annotation = "warning" if report.status != "failed" else "error"
            if os.getenv("GITHUB_ACTIONS") == "true":
                print(f"::{annotation} title=Paper update {report.status}::{report.message}")
        except (ArxivFetchError, PaperValidationError) as exc:
            report = self._failed_report(f"Paper update failed: {exc}")
            if os.getenv("GITHUB_ACTIONS") == "true":
                print(f"::error title=Paper update failed::{report.message}")
        except Exception as exc:
            report = self._failed_report(
                f"Update pipeline failed before publication: {exc}"
            )
            if os.getenv("GITHUB_ACTIONS") == "true":
                print(f"::error title=Paper update failed::{report.message}")

        self.write_report(report, report_path)
        self.logger.info("Update status: %s - %s", report.status, report.message)
        return report
