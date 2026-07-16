import datetime
import json
import logging
import os
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
logging.disable(logging.CRITICAL)

from arxiv_crawler import ArxivFetchError  # noqa: E402
from paper_data import (  # noqa: E402
    PaperValidationError,
    find_latest_valid_snapshot,
    normalized_arxiv_id,
    validate_papers,
)
from update_pipeline import UpdatePipeline  # noqa: E402


UTC = datetime.timezone.utc


def make_papers(count, published_date=None, start_index=0):
    if published_date is None:
        published_date = datetime.datetime.now(UTC).date().isoformat()
    papers = []
    for index in range(start_index, start_index + count):
        arxiv_id = f"2607.{index:05d}"
        papers.append({
            "title": f"Video generation paper {index}",
            "authors": ["Test Author"],
            "abstract": "A video diffusion method.",
            "arxiv_url": f"https://arxiv.org/abs/{arxiv_id}v1",
            "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}v1",
            "published_date": published_date,
            "categories": ["cs.CV"],
            "github_url": "",
            "keywords": ["video generation"],
            "citations": 0,
            "semantic_url": "",
            "links": {},
            "bibtex": "",
        })
    return papers


class FakeCrawler:
    def __init__(
        self,
        papers=None,
        error=None,
        catchup_papers=None,
        catchup_error=None,
    ):
        self.papers = papers
        self.error = error
        self.catchup_papers = catchup_papers or []
        self.catchup_error = catchup_error
        self.catchup_ranges = []

    def search_papers(self, max_results=None):
        if self.error is not None:
            raise self.error
        if max_results is None:
            return self.papers
        return self.papers[:max_results]

    def search_papers_between(self, date_from, date_to):
        self.catchup_ranges.append((date_from, date_to))
        if self.catchup_error is not None:
            raise self.catchup_error
        return self.catchup_papers

    def save_papers(self, papers, output_file=None):
        paper_dicts = validate_papers(papers)
        output_file = Path(output_file)
        output_file.write_text(
            json.dumps(paper_dicts, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return output_file


class FailingReadmeGenerator:
    def generate_readme(self, **kwargs):
        raise RuntimeError("render failed")


class UpdatePipelineTests(unittest.TestCase):
    def setUp(self):
        self.temporary_dir = tempfile.TemporaryDirectory()
        self.project_root = Path(self.temporary_dir.name)
        (self.project_root / "data").mkdir()
        (self.project_root / "README.md").write_text("stable readme\n", encoding="utf-8")
        (self.project_root / "README_template.md").write_text(
            "# Papers\n\n{{LAST_UPDATE}}\n\n{{NAVIGATION}}\n"
            "{{TABLE_OF_CONTENTS}}\n{{LATEST_PAPERS}}\n"
            "{{CATEGORIZED_PAPERS}}\n",
            encoding="utf-8",
        )
        keywords = {
            "categories": {
                "Video Generation": {
                    "description": "Video generation papers",
                    "keywords": ["video generation"],
                }
            },
            "common_keywords": {"keywords": ["video generation"]},
        }
        (self.project_root / "data" / "keywords.json").write_text(
            json.dumps(keywords), encoding="utf-8"
        )
        self.now = datetime.datetime(2026, 7, 15, 1, 0, tzinfo=UTC)

    def tearDown(self):
        self.temporary_dir.cleanup()

    def write_snapshot(self, date_value, papers=None, raw_content=None):
        path = self.project_root / "data" / f"papers_{date_value.isoformat()}.json"
        if raw_content is not None:
            path.write_text(raw_content, encoding="utf-8")
        else:
            path.write_text(
                json.dumps(papers or make_papers(1), ensure_ascii=False),
                encoding="utf-8",
            )
        return path

    def run_pipeline(self, crawler, readme_factory=None):
        pipeline = UpdatePipeline(
            project_root=self.project_root,
            crawler_factory=lambda: crawler,
            readme_factory=readme_factory,
            now_fn=lambda: self.now,
        )
        report_path = self.project_root / "update-report.json"
        report = pipeline.run(report_path=report_path)
        saved_report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertEqual(report.to_dict(), saved_report)
        return report

    def tracked_state(self):
        paths = [self.project_root / "README.md"]
        paths.extend(sorted((self.project_root / "data").glob("papers_*.json")))
        archive_path = self.project_root / "data" / "paper_archive.json"
        if archive_path.exists():
            paths.append(archive_path)
        return {path.relative_to(self.project_root): path.read_bytes() for path in paths}

    def test_successfully_publishes_500_papers_and_readme(self):
        report = self.run_pipeline(FakeCrawler(papers=make_papers(500)))

        data_path = self.project_root / "data" / "papers_2026-07-15.json"
        archive_path = self.project_root / "data" / "paper_archive.json"
        self.assertEqual("updated", report.status)
        self.assertEqual(500, report.paper_count)
        self.assertEqual(500, len(json.loads(data_path.read_text(encoding="utf-8"))))
        self.assertEqual(
            500,
            len(json.loads(archive_path.read_text(encoding="utf-8"))),
        )
        self.assertIn("Video generation paper 499", (
            self.project_root / "README.md"
        ).read_text(encoding="utf-8"))

    def test_bootstraps_archive_and_persists_every_catchup_paper(self):
        snapshot_date = self.now.date() - datetime.timedelta(days=5)
        historical = make_papers(
            1,
            published_date=snapshot_date.isoformat(),
            start_index=900,
        )
        self.write_snapshot(snapshot_date, papers=historical)
        crawler = FakeCrawler(
            papers=make_papers(2, start_index=0),
            catchup_papers=make_papers(
                1,
                published_date=(self.now.date() - datetime.timedelta(days=2)).isoformat(),
                start_index=500,
            ),
        )

        report = self.run_pipeline(crawler)

        archive_path = self.project_root / "data" / "paper_archive.json"
        archive = json.loads(archive_path.read_text(encoding="utf-8"))
        archive_ids = {
            normalized_arxiv_id(paper["arxiv_url"])
            for paper in archive
        }
        self.assertEqual("updated", report.status)
        self.assertEqual(
            {"2607.00000", "2607.00001", "2607.00500", "2607.00900"},
            archive_ids,
        )
        self.assertEqual([(snapshot_date, self.now.date())], crawler.catchup_ranges)
        self.assertIn(
            "Video generation paper 500",
            (self.project_root / "README.md").read_text(encoding="utf-8"),
        )

    def test_catchup_failure_preserves_existing_files(self):
        snapshot_date = self.now.date() - datetime.timedelta(days=1)
        self.write_snapshot(snapshot_date)
        before = self.tracked_state()

        report = self.run_pipeline(
            FakeCrawler(
                papers=make_papers(2),
                catchup_error=ArxivFetchError("catch-up unavailable"),
            )
        )

        self.assertEqual("degraded", report.status)
        self.assertEqual(before, self.tracked_state())

    def test_three_day_old_snapshot_degrades_without_modifying_files(self):
        self.write_snapshot(self.now.date() - datetime.timedelta(days=3))
        before = self.tracked_state()

        report = self.run_pipeline(
            FakeCrawler(error=ArxivFetchError("arXiv unavailable"))
        )

        self.assertEqual("degraded", report.status)
        self.assertEqual(3, report.stale_days)
        self.assertEqual(before, self.tracked_state())

    def test_four_day_old_snapshot_fails_without_modifying_files(self):
        self.write_snapshot(self.now.date() - datetime.timedelta(days=4))
        before = self.tracked_state()

        report = self.run_pipeline(
            FakeCrawler(error=ArxivFetchError("arXiv unavailable"))
        )

        self.assertEqual("failed", report.status)
        self.assertEqual(4, report.stale_days)
        self.assertEqual(before, self.tracked_state())

    def test_corrupt_newest_snapshot_is_skipped(self):
        valid_date = self.now.date() - datetime.timedelta(days=2)
        self.write_snapshot(valid_date)
        self.write_snapshot(
            self.now.date() - datetime.timedelta(days=1), raw_content="not json"
        )

        report = self.run_pipeline(
            FakeCrawler(error=ArxivFetchError("arXiv unavailable"))
        )

        self.assertEqual("degraded", report.status)
        self.assertEqual(valid_date.isoformat(), report.latest_data_date)

    def test_snapshot_selection_uses_filename_date_not_mtime(self):
        older = self.write_snapshot(self.now.date() - datetime.timedelta(days=2))
        newer = self.write_snapshot(self.now.date() - datetime.timedelta(days=1))
        os.utime(older, (newer.stat().st_mtime + 1000,) * 2)

        snapshot = find_latest_valid_snapshot(self.project_root / "data")

        self.assertEqual(newer, snapshot.path)

    def test_readme_failure_leaves_data_and_readme_unchanged(self):
        before = self.tracked_state()

        report = self.run_pipeline(
            FakeCrawler(papers=make_papers(1)),
            readme_factory=FailingReadmeGenerator,
        )

        self.assertEqual("failed", report.status)
        self.assertEqual(before, self.tracked_state())

    def test_invalid_fetched_data_is_not_published(self):
        duplicate_papers = make_papers(2)
        duplicate_papers[1]["arxiv_url"] = duplicate_papers[0]["arxiv_url"]

        report = self.run_pipeline(FakeCrawler(papers=duplicate_papers))

        self.assertEqual("failed", report.status)
        self.assertFalse(
            (self.project_root / "data" / "papers_2026-07-15.json").exists()
        )


class PaperValidationTests(unittest.TestCase):
    def test_rejects_invalid_date_and_missing_required_fields(self):
        invalid_cases = []
        invalid_date = make_papers(1)
        invalid_date[0]["published_date"] = "2026/07/15"
        invalid_cases.append(invalid_date)
        missing_title = make_papers(1)
        missing_title[0]["title"] = ""
        invalid_cases.append(missing_title)
        invalid_authors = make_papers(1)
        invalid_authors[0]["authors"] = "Test Author"
        invalid_cases.append(invalid_authors)

        for papers in invalid_cases:
            with self.subTest(papers=papers):
                with self.assertRaises(PaperValidationError):
                    validate_papers(papers)


if __name__ == "__main__":
    unittest.main()
