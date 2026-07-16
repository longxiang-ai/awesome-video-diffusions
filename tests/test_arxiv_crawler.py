import datetime
import logging
import sys
import tempfile
import unittest
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
logging.disable(logging.CRITICAL)

from arxiv_crawler import (  # noqa: E402
    ARXIV_API_URL,
    ARXIV_USER_AGENT,
    ArxivCrawler,
    ArxivFetchError,
)
from paper_data import PaperValidationError  # noqa: E402


class FakeResponse:
    def __init__(self, status_code=200, content=b"", headers=None):
        self.status_code = status_code
        self.content = content
        self.headers = headers or {}


class FakeSession:
    def __init__(self, responses):
        self.responses = list(responses)
        self.headers = {}
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        response = self.responses.pop(0)
        if isinstance(response, BaseException):
            raise response
        return response


def make_feed(total, start, count):
    published = (
        datetime.datetime.now(datetime.timezone.utc).date()
        - datetime.timedelta(days=1)
    ).isoformat()
    entries = []
    for offset in range(start, start + count):
        arxiv_id = f"2607.{offset:05d}"
        entries.append(
            f"""
            <entry>
              <id>https://arxiv.org/abs/{arxiv_id}v1</id>
              <updated>{published}T00:00:00Z</updated>
              <published>{published}T00:00:00Z</published>
              <title>Video generation paper {offset}</title>
              <summary>A video diffusion method.</summary>
              <author><name>Test Author</name></author>
              <link href="https://arxiv.org/abs/{arxiv_id}v1" rel="alternate" type="text/html" />
              <link title="pdf" href="https://arxiv.org/pdf/{arxiv_id}v1" rel="related" type="application/pdf" />
              <category term="cs.CV" />
            </entry>
            """
        )
    return (
        "<?xml version='1.0' encoding='UTF-8'?>"
        "<feed xmlns='http://www.w3.org/2005/Atom' "
        "xmlns:opensearch='http://a9.com/-/spec/opensearch/1.1/'>"
        f"<opensearch:totalResults>{total}</opensearch:totalResults>"
        + "".join(entries)
        + "</feed>"
    ).encode("utf-8")


class ArxivCrawlerTests(unittest.TestCase):
    def make_crawler(self, responses):
        self.sleeps = []
        self.session = FakeSession(responses)
        return ArxivCrawler(session=self.session, sleep_fn=self.sleeps.append)

    def test_fetches_complete_500_paper_page_over_https(self):
        crawler = self.make_crawler([FakeResponse(content=make_feed(500, 0, 500))])

        papers = crawler.search_papers(max_results=500)

        self.assertEqual(500, len(papers))
        self.assertEqual(ARXIV_API_URL, self.session.calls[0][0])
        self.assertEqual((10, 45), self.session.calls[0][1]["timeout"])
        self.assertEqual(ARXIV_USER_AGENT, self.session.headers["User-Agent"])
        self.assertEqual([], self.sleeps)
        self.assertEqual(
            sorted(papers[0].keywords, key=str.casefold),
            papers[0].keywords,
        )

    def test_retries_two_503_responses_then_succeeds(self):
        crawler = self.make_crawler([
            FakeResponse(status_code=503),
            FakeResponse(status_code=503),
            FakeResponse(content=make_feed(1, 0, 1)),
        ])

        papers = crawler.search_papers(max_results=1)

        self.assertEqual(1, len(papers))
        self.assertEqual([2.0, 4.0], self.sleeps)

    def test_caps_retry_after_at_60_seconds(self):
        crawler = self.make_crawler([
            FakeResponse(status_code=429, headers={"Retry-After": "120"}),
            FakeResponse(content=make_feed(1, 0, 1)),
        ])

        crawler.search_papers(max_results=1)

        self.assertEqual([60.0], self.sleeps)

    def test_paginates_and_waits_three_seconds_between_pages(self):
        crawler = self.make_crawler([
            FakeResponse(content=make_feed(501, 0, 500)),
            FakeResponse(content=make_feed(501, 500, 1)),
        ])

        papers = crawler.search_papers(max_results=501)

        self.assertEqual(501, len(papers))
        self.assertEqual([3.0], self.sleeps)
        self.assertEqual(500, self.session.calls[1][1]["params"]["start"])

    def test_catchup_query_fetches_every_result_in_inclusive_date_range(self):
        crawler = self.make_crawler([
            FakeResponse(content=make_feed(501, 0, 500)),
            FakeResponse(content=make_feed(501, 500, 1)),
        ])

        papers = crawler.search_papers_between(
            datetime.date(2026, 7, 10),
            datetime.date(2026, 7, 15),
        )

        self.assertEqual(501, len(papers))
        query = self.session.calls[0][1]["params"]["search_query"]
        self.assertIn("submittedDate:[202607100000 TO 202607152359]", query)
        self.assertEqual([3.0], self.sleeps)

    def test_catchup_query_accepts_a_valid_empty_result(self):
        crawler = self.make_crawler(
            [FakeResponse(content=make_feed(0, 0, 0))]
        )

        papers = crawler.search_papers_between(
            datetime.date(2026, 7, 15),
            datetime.date(2026, 7, 15),
        )

        self.assertEqual([], papers)
        self.assertEqual([], self.sleeps)

    def test_timeout_invalid_xml_and_empty_feed_never_return_empty_list(self):
        cases = [
            [requests.Timeout("timeout")] * 4,
            [FakeResponse(content=b"not xml")] * 4,
            [FakeResponse(content=make_feed(0, 0, 0))] * 4,
        ]
        for responses in cases:
            with self.subTest(responses=responses):
                crawler = self.make_crawler(responses)
                with self.assertRaises(ArxivFetchError):
                    crawler.search_papers(max_results=1)

    def test_save_rejects_empty_paper_list(self):
        crawler = self.make_crawler([])
        with tempfile.TemporaryDirectory() as temporary_dir:
            output_path = Path(temporary_dir) / "papers.json"
            with self.assertRaises(PaperValidationError):
                crawler.save_papers([], output_file=output_path)
            self.assertFalse(output_path.exists())


if __name__ == "__main__":
    unittest.main()
