import contextlib
import io
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import main as cli  # noqa: E402
from arxiv_crawler import (  # noqa: E402
    ArxivTemporaryError,
    SearchConfigurationError,
)


def args():
    return SimpleNamespace(
        citations=False,
        bibtex=False,
        date_from=None,
        date_to=None,
        recent=None,
        max_results=None,
    )


class FakeCrawler:
    def __init__(self, papers=None, error=None):
        self.papers = papers
        self.error = error
        self.saved = False

    def search_papers(self, max_results=None):
        if self.error:
            raise self.error
        return self.papers

    def save_papers(self, papers):
        self.saved = True


class SearchCliStatusTests(unittest.TestCase):
    def run_search(self, crawler=None, constructor_error=None):
        output = io.StringIO()
        patcher = mock.patch(
            "arxiv_crawler.ArxivCrawler",
            return_value=crawler,
            side_effect=constructor_error,
        )
        with patcher, contextlib.redirect_stdout(output):
            status = cli.cmd_search(args())
        return status, output.getvalue()

    def test_updated_returns_zero(self):
        crawler = FakeCrawler(papers=[object()])
        status, output = self.run_search(crawler=crawler)

        self.assertEqual(0, status)
        self.assertTrue(crawler.saved)
        self.assertIn("SEARCH_STATUS=updated", output)

    def test_no_results_returns_three_without_saving(self):
        crawler = FakeCrawler(papers=[])
        status, output = self.run_search(crawler=crawler)

        self.assertEqual(3, status)
        self.assertFalse(crawler.saved)
        self.assertIn("SEARCH_STATUS=no_results", output)

    def test_temporary_failure_returns_75(self):
        crawler = FakeCrawler(error=ArxivTemporaryError("rate limited"))
        status, output = self.run_search(crawler=crawler)

        self.assertEqual(75, status)
        self.assertIn("SEARCH_STATUS=temporary_failure", output)

    def test_configuration_error_returns_one(self):
        status, output = self.run_search(
            constructor_error=SearchConfigurationError("bad config")
        )

        self.assertEqual(1, status)
        self.assertIn("SEARCH_STATUS=error", output)


if __name__ == "__main__":
    unittest.main()
