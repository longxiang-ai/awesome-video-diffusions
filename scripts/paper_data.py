import datetime
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


SNAPSHOT_PATTERN = re.compile(r"papers_(\d{4}-\d{2}-\d{2})\.json$")


class PaperValidationError(ValueError):
    """Raised when a paper snapshot is unsafe to publish."""


@dataclass(frozen=True)
class ValidSnapshot:
    path: Path
    date: datetime.date
    papers: List[Dict[str, Any]]


def _paper_dict(paper: Any) -> Dict[str, Any]:
    if isinstance(paper, dict):
        return paper
    to_dict = getattr(paper, "to_dict", None)
    if callable(to_dict):
        return to_dict()
    raise PaperValidationError(f"Unsupported paper type: {type(paper).__name__}")


def validate_papers(papers: Iterable[Any]) -> List[Dict[str, Any]]:
    """Validate and return JSON-serializable paper dictionaries."""
    paper_dicts = [_paper_dict(paper) for paper in papers]
    if not paper_dicts:
        raise PaperValidationError("Paper list is empty")

    seen_ids = set()
    for index, paper in enumerate(paper_dicts):
        if not isinstance(paper, dict):
            raise PaperValidationError(f"Paper {index} is not an object")

        for field_name, label in (
            ("title", "title"),
            ("abstract", "abstract"),
            ("arxiv_url", "arXiv URL"),
            ("pdf_url", "PDF URL"),
        ):
            value = paper.get(field_name)
            if not isinstance(value, str) or not value.strip():
                raise PaperValidationError(f"Paper {index} has no {label}")
        arxiv_url = paper["arxiv_url"]

        date_value = paper.get("published_date")
        if not isinstance(date_value, str):
            raise PaperValidationError(f"Paper {index} has no publication date")
        try:
            parsed_date = datetime.date.fromisoformat(date_value)
        except ValueError as exc:
            raise PaperValidationError(
                f"Paper {index} has invalid publication date: {date_value}"
            ) from exc
        if parsed_date.isoformat() != date_value:
            raise PaperValidationError(
                f"Paper {index} publication date is not YYYY-MM-DD: {date_value}"
            )

        for field_name in ("authors", "categories"):
            value = paper.get(field_name)
            if (
                not isinstance(value, list)
                or not value
                or any(not isinstance(item, str) or not item.strip() for item in value)
            ):
                raise PaperValidationError(
                    f"Paper {index} field '{field_name}' must be a non-empty string list"
                )

        keywords = paper.get("keywords", [])
        if not isinstance(keywords, list) or any(
            not isinstance(keyword, str) or not keyword.strip() for keyword in keywords
        ):
            raise PaperValidationError(
                f"Paper {index} field 'keywords' must be a string list"
            )
        if "links" in paper and not isinstance(paper["links"], dict):
            raise PaperValidationError(f"Paper {index} field 'links' must be an object")

        arxiv_id = arxiv_url.rstrip("/").split("/")[-1]
        normalized_id = re.sub(r"v\d+$", "", arxiv_id)
        if not normalized_id:
            raise PaperValidationError(f"Paper {index} has an invalid arXiv URL")
        if normalized_id in seen_ids:
            raise PaperValidationError(f"Duplicate arXiv ID: {normalized_id}")
        seen_ids.add(normalized_id)

    return paper_dicts


def load_papers_file(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise PaperValidationError(f"Snapshot is not a list: {path}")
    return validate_papers(data)


def snapshot_date(path: Path) -> Optional[datetime.date]:
    match = SNAPSHOT_PATTERN.fullmatch(path.name)
    if not match:
        return None
    try:
        return datetime.date.fromisoformat(match.group(1))
    except ValueError:
        return None


def find_latest_valid_snapshot(data_dir: Path) -> Optional[ValidSnapshot]:
    candidates = []
    for path in data_dir.glob("papers_*.json"):
        date_value = snapshot_date(path)
        if date_value is not None:
            candidates.append((date_value, path))

    for date_value, path in sorted(candidates, reverse=True):
        try:
            papers = load_papers_file(path)
        except (OSError, json.JSONDecodeError, PaperValidationError):
            continue
        return ValidSnapshot(path=path, date=date_value, papers=papers)
    return None
