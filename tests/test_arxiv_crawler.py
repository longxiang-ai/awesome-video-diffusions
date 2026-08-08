import datetime
import logging
import tempfile
import unittest
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(ROOT / "scripts"))
logging.disable(logging.CRITICAL)

from arxiv_crawler import (  # noqa: E402
    ARXIV_API_URL,
    ARXIV_USER_AGENT,
    ArxivCrawler,
    ArxivFetchError,
    ArxivTemporaryError,
    Paper,
    SearchConfigurationError,
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


def make_entry(index, title=None, summary=None, published=None):
    if published is None:
        published = (
            datetime.datetime.now(datetime.timezone.utc).date()
            - datetime.timedelta(days=1)
        ).isoformat()
    title = title or f"Video generation paper {index}"
    summary = summary or "A video diffusion method for generative modeling."
    arxiv_id = f"2607.{index:05d}"
    return f"""
      <entry>
        <id>https://arxiv.org/abs/{arxiv_id}v1</id>
        <updated>{published}T00:00:00Z</updated>
        <published>{published}T00:00:00Z</published>
        <title>{title}</title>
        <summary>{summary}</summary>
        <author><name>Test Author</name></author>
        <link href="https://arxiv.org/abs/{arxiv_id}v1" rel="alternate" type="text/html" />
        <link title="pdf" href="https://arxiv.org/pdf/{arxiv_id}v1" rel="related" type="application/pdf" />
        <category term="cs.CV" />
      </entry>
    """


def make_feed(total, entries):
    return (
        "<?xml version='1.0' encoding='UTF-8'?>"
        "<feed xmlns='http://www.w3.org/2005/Atom' "
        "xmlns:opensearch='http://a9.com/-/spec/opensearch/1.1/'>"
        f"<opensearch:totalResults>{total}</opensearch:totalResults>"
        + "".join(entries)
        + "</feed>"
    ).encode("utf-8")


def make_video_feed(total, start, count):
    return make_feed(total, [make_entry(index) for index in range(start, start + count)])


def make_paper(title, abstract):
    return Paper(
        title=title,
        authors=["Test Author"],
        abstract=abstract,
        arxiv_url="https://arxiv.org/abs/2607.00001v1",
        pdf_url="https://arxiv.org/pdf/2607.00001v1",
        published_date="2026-07-01",
        categories=["cs.CV"],
    )


class ArxivCrawlerTests(unittest.TestCase):
    def make_crawler(self, responses, **kwargs):
        self.sleeps = []
        self.session = FakeSession(responses)
        return ArxivCrawler(
            session=self.session,
            sleep_fn=self.sleeps.append,
            data_dir=ROOT / "data",
            **kwargs,
        )

    def test_fetches_complete_page_over_https_with_date_and_domain_query(self):
        crawler = self.make_crawler(
            [FakeResponse(content=make_video_feed(500, 0, 500))]
        )

        papers = crawler.search_papers(max_results=500)

        self.assertEqual(500, len(papers))
        self.assertEqual(ARXIV_API_URL, self.session.calls[0][0])
        self.assertEqual((10, 45), self.session.calls[0][1]["timeout"])
        self.assertEqual(ARXIV_USER_AGENT, self.session.headers["User-Agent"])
        query = self.session.calls[0][1]["params"]["search_query"]
        self.assertIn("submittedDate:[", query)
        self.assertIn("cat:cs.RO", query)
        self.assertIn('abs:"video-to-video"', query)
        self.assertEqual([], self.sleeps)

    def test_retries_two_503_responses_then_succeeds(self):
        crawler = self.make_crawler([
            FakeResponse(status_code=503),
            FakeResponse(status_code=503),
            FakeResponse(content=make_video_feed(1, 0, 1)),
        ])

        papers = crawler.search_papers(max_results=1)

        self.assertEqual(1, len(papers))
        self.assertEqual([10.0, 30.0], self.sleeps)

    def test_honors_retry_after_up_to_300_seconds(self):
        crawler = self.make_crawler([
            FakeResponse(status_code=429, headers={"Retry-After": "400"}),
            FakeResponse(content=make_video_feed(1, 0, 1)),
        ])

        crawler.search_papers(max_results=1)

        self.assertEqual([300.0], self.sleeps)

    def test_persistent_timeout_is_temporary_failure(self):
        crawler = self.make_crawler([requests.Timeout("timeout")] * 4)

        with self.assertRaises(ArxivTemporaryError):
            crawler.search_papers(max_results=1)

        self.assertEqual([10.0, 30.0, 60.0], self.sleeps)

    def test_invalid_xml_and_non_retryable_http_are_fatal_without_retry(self):
        cases = [
            FakeResponse(content=b"not xml"),
            FakeResponse(status_code=404),
        ]
        for response in cases:
            with self.subTest(response=response.status_code):
                crawler = self.make_crawler([response])
                with self.assertRaises(ArxivFetchError):
                    crawler.search_papers(max_results=1)
                self.assertEqual(1, len(self.session.calls))
                self.assertEqual([], self.sleeps)

    def test_valid_empty_feed_returns_no_results(self):
        crawler = self.make_crawler([FakeResponse(content=make_feed(0, []))])

        self.assertEqual([], crawler.search_papers(max_results=1000))

    def test_paginates_until_1000_relevant_papers_are_collected(self):
        irrelevant = [
            make_entry(
                index,
                title=f"Adaptive Token Pruning for Video-Language Models {index}",
                summary="We compare against video generation systems.",
            )
            for index in range(500)
        ]
        crawler = self.make_crawler([
            FakeResponse(content=make_feed(1500, irrelevant)),
            FakeResponse(content=make_video_feed(1500, 500, 500)),
            FakeResponse(content=make_video_feed(1500, 1000, 500)),
        ])

        papers = crawler.search_papers(max_results=1000)

        self.assertEqual(1000, len(papers))
        self.assertEqual([3.0, 3.0], self.sleeps)
        self.assertEqual([0, 500, 1000], [
            call[1]["params"]["start"] for call in self.session.calls
        ])

    def test_relevance_filter_keeps_broad_generation_families(self):
        crawler = self.make_crawler([])
        positives = [
            make_paper(
                "Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models",
                "A unified model for native streaming video-generation and audio interaction.",
            ),
            make_paper(
                "AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation",
                "A tokenizer for synchronized audio and video.",
            ),
            make_paper(
                "Autoregressive Video Generation without Vector Quantization",
                "NOVA predicts frames autoregressively.",
            ),
            make_paper(
                "Cosmos World Foundation Model Platform for Physical AI",
                "The platform includes video tokenizers and generative world prediction.",
            ),
            make_paper(
                "BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning",
                "The simulator predicts video frames for embodied agents.",
            ),
            make_paper(
                "Video Models as Native 4D Renderers",
                "We use video diffusion models to synthesize dynamic 4D scenes.",
            ),
        ]

        for paper in positives:
            with self.subTest(title=paper.title):
                self.assertTrue(crawler._is_relevant_paper(paper))

    def test_relevance_filter_rejects_observed_false_positives(self):
        crawler = self.make_crawler([])
        negatives = [
            "Qwen-3D: A Generalist 3D Vision-Language Model for Spatial Understanding",
            "Adaptive Two-Stage Visual Token Pruning for Video-Language Models",
            "Estimating SSIM from MSE for DCT-Based Compressed Images",
            "SoccerNet 2026 Challenges Results",
        ]
        for title in negatives:
            paper = make_paper(title, "We compare our task with video generation models.")
            with self.subTest(title=title):
                self.assertFalse(crawler._is_relevant_paper(paper))

    def test_short_acronyms_match_only_complete_tokens(self):
        crawler = self.make_crawler([])

        false_matches = crawler._extract_keywords(
            "We make additional editing improvements.", "A baseline"
        )
        true_matches = crawler._extract_keywords(
            "A DiT model for T2V and I2V generation.", "Video generation"
        )

        self.assertNotIn("dit", false_matches)
        self.assertIn("dit", true_matches)
        self.assertIn("t2v", true_matches)
        self.assertIn("i2v", true_matches)

    def test_invalid_user_config_is_a_real_error(self):
        with tempfile.TemporaryDirectory() as temporary_dir:
            data_dir = Path(temporary_dir)
            (data_dir / "user_config.json").write_text("not json", encoding="utf-8")
            with self.assertRaises(SearchConfigurationError):
                ArxivCrawler(data_dir=data_dir)

    def test_save_rejects_empty_paper_list(self):
        crawler = self.make_crawler([])
        with tempfile.TemporaryDirectory() as temporary_dir:
            output_path = Path(temporary_dir) / "papers.json"
            with self.assertRaises(PaperValidationError):
                crawler.save_papers([], output_file=output_path)
            self.assertFalse(output_path.exists())


if __name__ == "__main__":
    unittest.main()
