import datetime
import email.utils
import json
import os
import re
import sys
import tempfile
import time
import requests
import argparse
import xml.etree.ElementTree as ET
from typing import Callable, List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict, field
from pathlib import Path
from utils.logger import setup_logger
from paper_data import PaperValidationError, validate_papers
from text_matching import contains_any, contains_phrase, normalize_text


ARXIV_API_URL = "https://export.arxiv.org/api/query"
ARXIV_PAGE_SIZE = 500
ARXIV_REQUEST_ATTEMPTS = 4
ARXIV_RETRY_DELAYS = (10.0, 30.0, 60.0)
EXIT_NO_RESULTS = 3
EXIT_TEMPORARY_FAILURE = 75
ARXIV_USER_AGENT = (
    "awesome-video-diffusions/1.0 "
    "(https://github.com/longxiang-ai/awesome-video-diffusions)"
)


class ArxivFetchError(RuntimeError):
    """Raised when a complete, valid arXiv result cannot be fetched."""


class ArxivTemporaryError(ArxivFetchError):
    """Raised for retryable arXiv or network failures."""


class SearchConfigurationError(ValueError):
    """Raised when the effective search configuration is invalid."""


@dataclass
class Paper:
    title: str
    authors: List[str]
    abstract: str
    arxiv_url: str
    pdf_url: str
    published_date: str
    categories: List[str]
    github_url: str = ""
    keywords: List[str] = None
    citations: int = 0
    semantic_url: str = ""
    links: Dict[str, str] = field(default_factory=dict)
    bibtex: str = ""

    def __post_init__(self):
        if self.keywords is None:
            self.keywords = []
        if self.links is None:
            self.links = {}

    def to_dict(self):
        return asdict(self)


def parse_relative_period(period_str: str) -> datetime.timedelta:
    """Parse a relative period string like '6m', '1y', '2y', '30d' into timedelta."""
    period_str = period_str.strip().lower()
    match = re.match(r'^(\d+)\s*([dmy])$', period_str)
    if not match:
        raise ValueError(f"Invalid period format: '{period_str}'. Use format like '30d', '6m', '1y', '2y'.")
    value = int(match.group(1))
    unit = match.group(2)
    if unit == 'd':
        return datetime.timedelta(days=value)
    elif unit == 'm':
        return datetime.timedelta(days=value * 30)
    elif unit == 'y':
        return datetime.timedelta(days=value * 365)
    raise ValueError(f"Unknown unit: {unit}")


class ArxivCrawler:
    def __init__(self, fetch_citations: bool = False, fetch_bibtex: bool = False,
                 date_from: str = None, date_to: str = None, recent: str = None,
                 session: Optional[requests.Session] = None,
                 sleep_fn: Callable[[float], None] = time.sleep,
                 data_dir: Path = Path("data")):
        self.logger = setup_logger("arxiv_crawler")
        self.output_dir = Path(data_dir)
        self.output_dir.mkdir(exist_ok=True)

        self.user_config = self._load_user_config()
        self.date_start, self.date_end = self._resolve_time_range(date_from, date_to, recent)
        self.search_query = self._load_search_config()

        self.github_token = os.getenv("GITHUB_TOKEN")
        self.github_headers = {
            "Authorization": f"token {self.github_token}" if self.github_token else "",
            "Accept": "application/vnd.github.v3+json"
        }
        self.fetch_citations = fetch_citations
        self.fetch_bibtex = fetch_bibtex
        self.semantic_api_url = "https://api.semanticscholar.org/v1/paper/arXiv:"
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": ARXIV_USER_AGENT})
        self.sleep_fn = sleep_fn

        # Load keywords configuration
        try:
            keywords_path = self.output_dir / "keywords.json"
            if not keywords_path.exists():
                self.logger.error(f"Keywords file not found: {keywords_path}")
                raise FileNotFoundError(f"Keywords file not found: {keywords_path}")

            with open(keywords_path, "r", encoding="utf-8") as f:
                keywords_data = json.load(f)
                self.common_keywords = keywords_data["common_keywords"]["keywords"]
                self.category_keywords = {
                    category: info["keywords"]
                    for category, info in keywords_data["categories"].items()
                }
                self.logger.info(f"Successfully loaded keywords configuration")
        except Exception as e:
            self.logger.error(f"Failed to load keywords configuration: {e}")
            raise

    def _load_user_config(self) -> dict:
        """Load user_config.json if it exists."""
        config_path = self.output_dir / "user_config.json"
        if not config_path.exists():
            return {}
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
        except (OSError, json.JSONDecodeError) as exc:
            raise SearchConfigurationError(
                f"Failed to load {config_path}: {exc}"
            ) from exc
        if not isinstance(config, dict):
            raise SearchConfigurationError(f"{config_path} must contain a JSON object")
        self.logger.info("Loaded user_config.json")
        return config

    @staticmethod
    def _validate_keyword_list(value, label: str) -> List[str]:
        if not isinstance(value, list):
            raise SearchConfigurationError(f"{label} must be a JSON array")
        result = []
        seen = set()
        for index, keyword in enumerate(value):
            if not isinstance(keyword, str) or not keyword.strip():
                raise SearchConfigurationError(
                    f"{label}[{index}] must be a non-empty string"
                )
            keyword = keyword.strip()
            if '"' in keyword:
                raise SearchConfigurationError(f'{label}[{index}] must not contain "')
            key = keyword.casefold()
            if key not in seen:
                seen.add(key)
                result.append(keyword)
        return result

    @classmethod
    def _validate_relevance_filter(cls, value, label: str) -> Dict[str, List[str]]:
        if not isinstance(value, dict):
            raise SearchConfigurationError(f"{label} must be a JSON object")
        required = (
            "strong_phrases",
            "conditional_title_phrases",
            "excluded_title_phrases",
            "video_evidence_phrases",
            "generation_evidence_phrases",
        )
        validated = {
            key: cls._validate_keyword_list(value.get(key), f"{label}.{key}")
            for key in required
        }
        if any(not phrases for phrases in validated.values()):
            raise SearchConfigurationError(f"Every {label} phrase list must be non-empty")
        return validated

    def _load_search_config(self) -> str:
        """从配置文件加载搜索配置并生成搜索查询。优先使用 user_config.json。"""
        config_path = self.output_dir / "search_config.json"
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                fallback_config = json.load(f)
        except (OSError, json.JSONDecodeError) as exc:
            raise SearchConfigurationError(
                f"Failed to load {config_path}: {exc}"
            ) from exc
        if not isinstance(fallback_config, dict):
            raise SearchConfigurationError(f"{config_path} must contain a JSON object")

        fallback_keywords = fallback_config.get("search_config")
        user_search = self.user_config.get("search", {})
        if not isinstance(user_search, dict):
            raise SearchConfigurationError("user_config.search must be a JSON object")
        user_keywords = user_search.get("keywords")
        if user_keywords is not None and not isinstance(user_keywords, dict):
            raise SearchConfigurationError(
                "user_config.search.keywords must be a JSON object"
            )
        if isinstance(user_keywords, dict) and any(user_keywords.get(key) for key in (
            "both_abstract_and_title", "abstract_only", "title_only"
        )):
            keyword_config = user_keywords
            self.logger.info("Using keywords from user_config.json")
        else:
            keyword_config = fallback_keywords
            self.logger.info("Using keywords from search_config.json")
        if not isinstance(keyword_config, dict):
            raise SearchConfigurationError("Effective search keywords must be a JSON object")

        both_keywords = self._validate_keyword_list(
            keyword_config.get("both_abstract_and_title"),
            "effective_keywords.both_abstract_and_title",
        )
        abs_keywords = self._validate_keyword_list(
            keyword_config.get("abstract_only"),
            "effective_keywords.abstract_only",
        )
        title_keywords = self._validate_keyword_list(
            keyword_config.get("title_only"),
            "effective_keywords.title_only",
        )
        if not (both_keywords or abs_keywords or title_keywords):
            raise SearchConfigurationError("No effective search keywords are configured")

        relevance_config = user_search.get("relevance_filter")
        if relevance_config is None:
            relevance_config = fallback_config.get("relevance_filter")
        self.relevance_filter = self._validate_relevance_filter(
            relevance_config, "effective_relevance_filter"
        )
        conditional_keys = {
            normalize_text(phrase)
            for phrase in self.relevance_filter["conditional_title_phrases"]
        }
        strong_keys = {
            normalize_text(phrase)
            for phrase in self.relevance_filter["strong_phrases"]
        }
        for keyword in both_keywords + abs_keywords + title_keywords:
            key = normalize_text(keyword)
            if key not in conditional_keys and key not in strong_keys:
                self.relevance_filter["strong_phrases"].append(keyword)
                strong_keys.add(key)

        domains = user_search.get("domains", [])
        if not isinstance(domains, list) or any(
            not isinstance(domain, str)
            or not re.fullmatch(r"[a-z-]+\.[A-Za-z-]+", domain)
            for domain in domains
        ):
            raise SearchConfigurationError("search.domains must contain valid arXiv categories")

        query_parts = []
        seen_parts = set()

        def add_part(field: str, keyword: str) -> None:
            part = f'{field}:"{keyword}"'
            key = part.casefold()
            if key not in seen_parts:
                seen_parts.add(key)
                query_parts.append(part)

        for keyword in both_keywords:
            add_part("abs", keyword)
            add_part("ti", keyword)
        for keyword in abs_keywords:
            add_part("abs", keyword)
        for keyword in title_keywords:
            add_part("ti", keyword)

        clauses = ["(" + " OR ".join(query_parts) + ")"]
        if domains:
            clauses.append("(" + " OR ".join(f"cat:{domain}" for domain in domains) + ")")
        if self.date_start or self.date_end:
            start = self.date_start or datetime.datetime(1900, 1, 1)
            end = self.date_end or datetime.datetime(3000, 12, 31, 23, 59, 59)
            clauses.append(
                f"submittedDate:[{start.strftime('%Y%m%d%H%M')} TO "
                f"{end.strftime('%Y%m%d%H%M')}]"
            )

        search_query = " AND ".join(clauses)
        self.logger.info("Generated search query from config: %s", search_query)
        return search_query

    def _resolve_time_range(self, date_from: str = None, date_to: str = None,
                            recent: str = None) -> Tuple[Optional[datetime.datetime], Optional[datetime.datetime]]:
        """Resolve time range from CLI args or user_config.json.

        CLI arguments take highest priority, then user_config.json.

        Returns:
            (start_date, end_date) — either or both may be None (no filter).
        """
        # Use date-only (midnight) to avoid boundary issues:
        # paper dates are parsed as "YYYY-MM-DD" (midnight 00:00:00),
        # so comparing against datetime.now() with a time component
        # would incorrectly exclude papers published on the boundary day.
        today = datetime.datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)

        # CLI --recent overrides everything
        if recent:
            try:
                delta = parse_relative_period(recent)
                start = (today - delta).replace(hour=0, minute=0, second=0, microsecond=0)
                self.logger.info(f"Time filter (CLI --recent): {start.strftime('%Y-%m-%d')} to {today.strftime('%Y-%m-%d')}")
                return start, today
            except ValueError as exc:
                raise SearchConfigurationError(str(exc)) from exc

        # CLI --date-from / --date-to
        if date_from or date_to:
            start = None
            end = None
            if date_from:
                try:
                    start = datetime.datetime.strptime(date_from, "%Y-%m-%d")
                except ValueError as exc:
                    raise SearchConfigurationError(
                        f"Invalid --date-from: {date_from}"
                    ) from exc
            if date_to:
                try:
                    end = datetime.datetime.strptime(date_to, "%Y-%m-%d").replace(
                        hour=23, minute=59, second=59
                    )
                except ValueError as exc:
                    raise SearchConfigurationError(
                        f"Invalid --date-to: {date_to}"
                    ) from exc
            if start and end and start > end:
                raise SearchConfigurationError("--date-from must not be after --date-to")
            if start or end:
                self.logger.info(f"Time filter (CLI): {start} to {end}")
                return start, end

        # user_config.json
        tr = self.user_config.get("search", {}).get("time_range", {})
        mode = tr.get("mode", "none")

        if mode == "relative":
            period = tr.get("relative", "1y")
            if period:
                try:
                    delta = parse_relative_period(period)
                    start = (today - delta).replace(hour=0, minute=0, second=0, microsecond=0)
                    self.logger.info(f"Time filter (config relative={period}): {start.strftime('%Y-%m-%d')} to {today.strftime('%Y-%m-%d')}")
                    return start, today
                except ValueError as exc:
                    raise SearchConfigurationError(
                        f"Invalid relative period in config: {exc}"
                    ) from exc

        elif mode == "absolute":
            start = None
            end = None
            if tr.get("start_date"):
                try:
                    start = datetime.datetime.strptime(tr["start_date"], "%Y-%m-%d")
                except ValueError as exc:
                    raise SearchConfigurationError(
                        f"Invalid configured start_date: {tr['start_date']}"
                    ) from exc
            if tr.get("end_date"):
                try:
                    end = datetime.datetime.strptime(tr["end_date"], "%Y-%m-%d").replace(
                        hour=23, minute=59, second=59
                    )
                except ValueError as exc:
                    raise SearchConfigurationError(
                        f"Invalid configured end_date: {tr['end_date']}"
                    ) from exc
            if start and end and start > end:
                raise SearchConfigurationError(
                    "Configured start_date must not be after end_date"
                )
            if start or end:
                self.logger.info(f"Time filter (config absolute): {start} to {end}")
                return start, end

        elif mode != "none":
            raise SearchConfigurationError(f"Invalid time_range.mode: {mode}")

        # No time filter
        self.logger.info("No time filter applied")
        return None, None

    def _filter_by_date(self, papers: List['Paper']) -> List['Paper']:
        """Filter papers by the resolved time range."""
        if not self.date_start and not self.date_end:
            return papers

        filtered = []
        for paper in papers:
            try:
                pub_date = datetime.datetime.strptime(paper.published_date, "%Y-%m-%d")
            except (ValueError, TypeError):
                filtered.append(paper)  # keep papers with unparseable dates
                continue

            if self.date_start and pub_date < self.date_start:
                continue
            if self.date_end and pub_date > self.date_end:
                continue
            filtered.append(paper)

        self.logger.info(f"Date filter: {len(papers)} -> {len(filtered)} papers")
        return filtered

    # ------------------------------------------------------------------ #
    #  Link extraction
    # ------------------------------------------------------------------ #

    def _extract_all_links(self, abstract: str, arxiv_url: str, pdf_url: str,
                           title: str = "") -> Dict[str, str]:
        """Extract and classify all links from abstract, plus known arxiv/pdf links."""
        links: Dict[str, str] = {}

        # Always add arxiv and pdf
        if arxiv_url:
            links["arxiv"] = arxiv_url
        if pdf_url:
            links["pdf"] = pdf_url

        # Extract all URLs from abstract
        search_text = f"{abstract} {title}"
        url_pattern = r'https?://[^\s<>"\)\]}\',;]+'
        raw_urls = re.findall(url_pattern, search_text)

        for url in raw_urls:
            url = self._clean_url(url)
            if not url:
                continue

            url_lower = url.lower()

            # Skip arxiv links (already have them)
            if 'arxiv.org' in url_lower:
                continue

            # GitHub
            if 'github.com' in url_lower or 'raw.githubusercontent.com' in url_lower:
                if 'github' not in links:
                    cleaned = self._clean_github_url(url)
                    if cleaned:
                        links['github'] = cleaned
                continue

            # HuggingFace datasets
            if 'huggingface.co/datasets' in url_lower:
                if 'dataset' not in links:
                    links['dataset'] = url
                continue

            # HuggingFace (non-dataset)
            if 'huggingface.co' in url_lower:
                if 'huggingface' not in links:
                    links['huggingface'] = url
                continue

            # Video links
            if any(domain in url_lower for domain in ['youtube.com', 'youtu.be', 'bilibili.com']):
                if 'video' not in links:
                    links['video'] = url
                continue

            # Dataset keywords in URL
            if any(kw in url_lower for kw in ['dataset', 'data', 'benchmark']):
                if 'dataset' not in links:
                    links['dataset'] = url
                continue

            # Demo/online tool
            if any(kw in url_lower for kw in ['demo', 'app', 'gradio', 'streamlit']):
                if 'demo' not in links:
                    links['demo'] = url
                continue

            # Everything else -> project page
            if 'project' not in links:
                links['project'] = url

        return links

    def _clean_url(self, url: str) -> Optional[str]:
        """Clean a raw URL extracted from text."""
        if not url:
            return None
        # Remove trailing punctuation that got captured
        url = re.sub(r'[.,;:!?\)\]\}]+$', '', url)
        url = url.rstrip('/')
        if len(url) < 10:
            return None
        return url

    def _find_github_url(self, text: str, title: str = "") -> Optional[str]:
        """从文本中查找GitHub链接"""
        # 合并所有可能包含GitHub链接的文本
        search_text = f"{text} {title}"

        # 添加更多常见的代码链接引导语
        code_indicators = [
            "code", "implementation", "source", "github", "repository",
            "official", "project", "available at", "released at"
        ]

        # 直接查找GitHub链接的正则表达式
        patterns = [
            r'(?:https?://)?github\.com/[\w-]+/[\w.-]+(?:/[^\s\)\]]*)?',
            r'(?:https?://)?raw\.githubusercontent\.com/[\w-]+/[\w.-]+',
            r'(?:https?://)?gist\.github\.com/[\w-]+/[\w.-]+',
        ]

        # 首先在代码指示词附近查找
        for indicator in code_indicators:
            idx = search_text.lower().find(indicator)
            if idx != -1:
                context = search_text[max(0, idx-200):min(len(search_text), idx+200)]
                for pattern in patterns:
                    matches = re.finditer(pattern, context, re.IGNORECASE)
                    for match in matches:
                        url = self._clean_github_url(match.group(0))
                        if url:
                            return url

        # 如果没找到，在整个文本中查找
        for pattern in patterns:
            matches = re.finditer(pattern, search_text, re.IGNORECASE)
            for match in matches:
                url = self._clean_github_url(match.group(0))
                if url:
                    return url

        return None

    def _clean_github_url(self, url: str) -> Optional[str]:
        """清理和验证GitHub URL"""
        try:
            if not url.startswith('http'):
                url = 'https://' + url

            url = url.rstrip('/')
            url = re.sub(r'[.,;:\)]$', '', url)
            url = url.split('#')[0]
            url = url.split('?')[0]

            if '/blob/' in url or '/tree/' in url:
                url = url.split('/blob/')[0] if '/blob/' in url else url.split('/tree/')[0]

            return url
        except Exception as e:
            self.logger.error(f"清理GitHub URL时出错: {e}")
            return None

    def _verify_github_repo(self, url: str) -> bool:
        """验证GitHub仓库是否存在"""
        try:
            parts = url.split('github.com/')[-1].split('/')
            if len(parts) < 2:
                return False

            owner, repo = parts[0], parts[1]
            repo = repo.split('#')[0].split('?')[0]

            if not self.github_token:
                self.logger.warning("未设置GitHub token，跳过仓库验证")
                return True

            api_url = f"https://api.github.com/repos/{owner}/{repo}"
            response = requests.get(api_url, headers=self.github_headers)
            if response.status_code == 200:
                self.logger.info(f"验证GitHub仓库成功: {owner}/{repo}")
                return True
            elif response.status_code == 403:
                self.logger.warning(f"GitHub API rate limit exceeded，跳过验证: {owner}/{repo}")
                return True
            else:
                self.logger.warning(f"GitHub仓库不存在或无法访问: {owner}/{repo} (状态码: {response.status_code})")
                return False

        except Exception as e:
            self.logger.error(f"验证GitHub仓库时出错: {e}")
            return True

    def _get_citations(self, arxiv_id: str) -> tuple:
        """获取论文引用数"""
        if not self.fetch_citations:
            return 0, ''

        try:
            response = requests.get(f"{self.semantic_api_url}{arxiv_id}")
            if response.status_code == 200:
                data = response.json()
                return data.get('citationCount', 0), data.get('url', '')
            return 0, ''
        except Exception as e:
            self.logger.error(f"获取引用数时出错: {e}")
            return 0, ''

    def _extract_keywords(self, abstract: str, title: str) -> List[str]:
        """Extract boundary-aware category keywords from abstract and title."""
        keywords = set()
        text = abstract + " " + title

        for keyword in self.common_keywords:
            if contains_phrase(text, keyword):
                keywords.add(keyword)

        for category_keywords in self.category_keywords.values():
            for keyword in category_keywords:
                if contains_phrase(text, keyword):
                    keywords.add(keyword)

        return sorted(keywords, key=str.casefold)

    def _is_relevant_paper(self, paper: Paper) -> bool:
        """Apply conservative local filtering to broad arXiv candidates."""
        title = paper.title
        abstract = paper.abstract
        strong = self.relevance_filter["strong_phrases"]
        if contains_any(title, strong):
            return True

        if contains_any(title, self.relevance_filter["excluded_title_phrases"]):
            return False

        if contains_any(abstract, strong):
            return True

        conditional = self.relevance_filter["conditional_title_phrases"]
        return (
            contains_any(title, conditional)
            and contains_any(abstract, self.relevance_filter["video_evidence_phrases"])
            and contains_any(
                abstract, self.relevance_filter["generation_evidence_phrases"]
            )
        )

    # ------------------------------------------------------------------ #
    #  BibTeX
    # ------------------------------------------------------------------ #

    def _fetch_bibtex(self, arxiv_id: str) -> str:
        """Fetch BibTeX entry from arXiv for a given paper ID."""
        # Strip version suffix (e.g. 2411.09156v1 -> 2411.09156)
        clean_id = re.sub(r'v\d+$', '', arxiv_id)
        url = f"https://arxiv.org/bibtex/{clean_id}"
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                bib = response.text.strip()
                if bib.startswith('@'):
                    return bib
                self.logger.warning(f"Unexpected BibTeX response for {clean_id}")
                return ""
            else:
                self.logger.warning(f"BibTeX fetch failed for {clean_id}: HTTP {response.status_code}")
                return ""
        except Exception as e:
            self.logger.error(f"BibTeX fetch error for {clean_id}: {e}")
            return ""

    def _get_arxiv_id(self, arxiv_url: str) -> str:
        """Extract arXiv ID from URL."""
        # Handle URLs like http://arxiv.org/abs/2411.09156v1
        return arxiv_url.rstrip('/').split('/')[-1]

    # ------------------------------------------------------------------ #
    #  Search methods
    # ------------------------------------------------------------------ #

    def _retry_after_seconds(self, response: Optional[requests.Response]) -> Optional[float]:
        if response is None:
            return None
        value = response.headers.get("Retry-After")
        if not value:
            return None
        try:
            return min(300.0, max(0.0, float(value)))
        except ValueError:
            try:
                retry_at = email.utils.parsedate_to_datetime(value)
                if retry_at.tzinfo is None:
                    retry_at = retry_at.replace(tzinfo=datetime.timezone.utc)
                now = datetime.datetime.now(datetime.timezone.utc)
                return min(300.0, max(0.0, (retry_at - now).total_seconds()))
            except (TypeError, ValueError, OverflowError):
                return None

    def _parse_arxiv_entry(self, entry: ET.Element) -> Paper:
        namespaces = {"atom": "http://www.w3.org/2005/Atom"}
        title = entry.findtext("atom:title", default="", namespaces=namespaces).strip()
        abstract = entry.findtext(
            "atom:summary", default="", namespaces=namespaces
        ).strip().replace("\n", " ")
        published = entry.findtext(
            "atom:published", default="", namespaces=namespaces
        ).strip()

        authors = []
        for author in entry.findall("atom:author", namespaces):
            name = author.findtext("atom:name", default="", namespaces=namespaces).strip()
            if name:
                authors.append(name)

        arxiv_url = ""
        pdf_url = ""
        for link in entry.findall("atom:link", namespaces):
            href = link.get("href", "")
            if link.get("rel", "") == "alternate":
                arxiv_url = href
            elif link.get("title") == "pdf":
                pdf_url = href

        categories = [
            category.get("term", "")
            for category in entry.findall("atom:category", namespaces)
            if category.get("term", "")
        ]
        keywords = self._extract_keywords(abstract, title)
        github_url = self._find_github_url(abstract, title) or ""
        all_links = self._extract_all_links(abstract, arxiv_url, pdf_url, title)
        if github_url and "github" not in all_links:
            all_links["github"] = github_url

        arxiv_id = self._get_arxiv_id(arxiv_url) if arxiv_url else ""
        citations, semantic_url = (
            self._get_citations(arxiv_id) if self.fetch_citations and arxiv_id else (0, "")
        )
        bibtex = ""
        if self.fetch_bibtex and arxiv_id:
            bibtex = self._fetch_bibtex(arxiv_id)
            self.sleep_fn(0.3)

        return Paper(
            title=title,
            authors=authors,
            abstract=abstract,
            arxiv_url=arxiv_url,
            pdf_url=pdf_url,
            published_date=published[:10],
            categories=categories,
            github_url=github_url,
            keywords=keywords,
            citations=citations,
            semantic_url=semantic_url,
            links=all_links,
            bibtex=bibtex,
        )

    def _parse_arxiv_page(
        self, content: bytes, start: int, page_size: int
    ) -> Tuple[List[Paper], int]:
        root = ET.fromstring(content)
        namespaces = {
            "atom": "http://www.w3.org/2005/Atom",
            "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
        }
        total_text = root.findtext("opensearch:totalResults", namespaces=namespaces)
        if total_text is None:
            raise ArxivFetchError("arXiv response has no totalResults")
        try:
            total_results = int(total_text)
        except ValueError as exc:
            raise ArxivFetchError(
                f"Invalid arXiv totalResults value: {total_text}"
            ) from exc
        if total_results < 0:
            raise ArxivFetchError("arXiv totalResults must not be negative")

        entries = root.findall("atom:entry", namespaces)
        expected_entries = min(page_size, max(0, total_results - start))
        if len(entries) != expected_entries:
            raise ArxivFetchError(
                f"Incomplete arXiv page at offset {start}: "
                f"expected {expected_entries}, received {len(entries)}"
            )

        papers = [self._parse_arxiv_entry(entry) for entry in entries]
        if papers:
            validate_papers(papers)
        return papers, total_results

    def _request_arxiv_page(
        self, start: int, page_size: int
    ) -> Tuple[List[Paper], int]:
        params = {
            "search_query": self.search_query,
            "start": start,
            "max_results": page_size,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        for attempt in range(ARXIV_REQUEST_ATTEMPTS):
            response = None
            try:
                self.logger.info(
                    "Requesting arXiv offset %s, size %s (attempt %s/%s)",
                    start,
                    page_size,
                    attempt + 1,
                    ARXIV_REQUEST_ATTEMPTS,
                )
                response = self.session.get(
                    ARXIV_API_URL,
                    params=params,
                    timeout=(10, 45),
                )
            except (requests.Timeout, requests.ConnectionError) as exc:
                if attempt == ARXIV_REQUEST_ATTEMPTS - 1:
                    raise ArxivTemporaryError(
                        f"arXiv network request failed after {attempt + 1} attempts: {exc}"
                    ) from exc
                delay = ARXIV_RETRY_DELAYS[attempt]
                self.logger.warning(
                    "arXiv request failed: %s. Retrying in %.1f seconds.",
                    exc,
                    delay,
                )
                self.sleep_fn(delay)
                continue

            if response.status_code == 429 or 500 <= response.status_code < 600:
                if attempt == ARXIV_REQUEST_ATTEMPTS - 1:
                    raise ArxivTemporaryError(
                        f"arXiv returned HTTP {response.status_code} after "
                        f"{attempt + 1} attempts"
                    )
                retry_after = self._retry_after_seconds(response)
                delay = (
                    retry_after
                    if retry_after is not None
                    else ARXIV_RETRY_DELAYS[attempt]
                )
                self.logger.warning(
                    "arXiv returned HTTP %s. Retrying in %.1f seconds.",
                    response.status_code,
                    delay,
                )
                self.sleep_fn(delay)
                continue

            if response.status_code != 200:
                raise ArxivFetchError(
                    f"Non-retryable arXiv HTTP status: {response.status_code}"
                )

            try:
                return self._parse_arxiv_page(response.content, start, page_size)
            except ET.ParseError as exc:
                raise ArxivFetchError(f"Invalid arXiv XML response: {exc}") from exc

        raise ArxivTemporaryError("arXiv request attempts were exhausted")

    def search_papers(self, max_results: int = None) -> List[Paper]:
        """Search papers on arXiv.

        Priority for max_results: explicit argument > user_config.json > default (1000).
        """
        if max_results is None:
            config_max = self.user_config.get("search", {}).get("max_results")
            max_results = config_max if config_max else 1000

        if not isinstance(max_results, int) or max_results <= 0:
            raise ArxivFetchError(f"max_results must be positive, got {max_results}")

        papers: List[Paper] = []
        seen_urls = set()
        total_available: Optional[int] = None
        start = 0

        while len(papers) < max_results and (
            total_available is None or start < total_available
        ):
            page_size = ARXIV_PAGE_SIZE
            if total_available is not None:
                page_size = min(page_size, total_available - start)
            page, page_total = self._request_arxiv_page(start, page_size)
            if total_available is None:
                total_available = page_total
            elif page_total != total_available:
                raise ArxivTemporaryError(
                    f"arXiv totalResults changed from {total_available} to {page_total}"
                )

            if total_available == 0:
                return []

            for paper in self._filter_by_date(page):
                if paper.arxiv_url in seen_urls or not self._is_relevant_paper(paper):
                    continue
                seen_urls.add(paper.arxiv_url)
                papers.append(paper)
                if len(papers) == max_results:
                    break

            start += len(page)
            if not page and start < total_available:
                raise ArxivTemporaryError(
                    f"arXiv returned an empty page before offset {total_available}"
                )
            if len(papers) < max_results and start < total_available:
                self.sleep_fn(3.0)

        if not papers:
            self.logger.warning("arXiv returned no relevant papers")
            return []
        validate_papers(papers)
        self.logger.info("Total papers collected: %s", len(papers))
        return papers

    def save_papers(
        self, papers: List[Paper], output_file: Optional[Path] = None
    ) -> Path:
        """Validate and atomically save paper data."""
        papers_dict = validate_papers(papers)
        if output_file is None:
            today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
            output_file = self.output_dir / f"papers_{today}.json"
        output_file = Path(output_file)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        temporary_path = None
        try:
            with tempfile.NamedTemporaryFile(
                "w",
                encoding="utf-8",
                dir=output_file.parent,
                prefix=f".{output_file.name}.",
                suffix=".tmp",
                delete=False,
            ) as handle:
                temporary_path = Path(handle.name)
                json.dump(papers_dict, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
            os.replace(temporary_path, output_file)
            self.logger.info(
                "Saved %s validated papers to %s", len(papers_dict), output_file
            )
            return output_file
        finally:
            if temporary_path is not None and temporary_path.exists():
                temporary_path.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description='arXiv论文爬虫')
    parser.add_argument('--citations', action='store_true',
                        help='是否获取引用数和Semantic Scholar链接')
    parser.add_argument('--bibtex', action='store_true',
                        help='是否获取每篇论文的BibTeX引用')
    parser.add_argument('--max-results', type=int, default=None,
                        help='最大获取论文数量（默认从user_config.json读取，否则1000）')
    parser.add_argument('--date-from', type=str, default=None,
                        help='检索起始日期 (YYYY-MM-DD)')
    parser.add_argument('--date-to', type=str, default=None,
                        help='检索结束日期 (YYYY-MM-DD)')
    parser.add_argument('--recent', type=str, default=None,
                        help='检索最近时间段，如 30d, 6m, 1y, 2y')
    args = parser.parse_args()

    try:
        crawler = ArxivCrawler(
            fetch_citations=args.citations,
            fetch_bibtex=args.bibtex,
            date_from=args.date_from,
            date_to=args.date_to,
            recent=args.recent
        )
        papers = crawler.search_papers(max_results=args.max_results)
        if not papers:
            print("SEARCH_STATUS=no_results")
            print("[WARN] arXiv returned no relevant papers; existing data was preserved.")
            return EXIT_NO_RESULTS
        crawler.save_papers(papers)
        print("SEARCH_STATUS=updated")
        print(f"[OK] Saved {len(papers)} papers.")
        return 0
    except ArxivTemporaryError as exc:
        print("SEARCH_STATUS=temporary_failure")
        print(f"[WARN] Temporary arXiv failure; existing data was preserved: {exc}")
        return EXIT_TEMPORARY_FAILURE
    except Exception as e:
        print("SEARCH_STATUS=error")
        print(f"[ERROR] Search failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
