import datetime
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence


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


def normalized_arxiv_id(arxiv_url: str) -> str:
    """Return an arXiv ID without its version suffix."""
    arxiv_id = arxiv_url.rstrip("/").split("/")[-1]
    return re.sub(r"v\d+$", "", arxiv_id)


def validate_papers(papers: Iterable[Any]) -> List[Dict[str, Any]]:
    """Validate and return JSON-serializable paper dictionaries."""
    paper_dicts = [_paper_dict(paper) for paper in papers]
    if not paper_dicts:
        raise PaperValidationError("Paper list is empty")

    seen_ids = set()
    for index, paper in enumerate(paper_dicts):
        if not isinstance(paper, dict):
            raise PaperValidationError(f"Paper {index} is not an object")

        title = paper.get("title")
        arxiv_url = paper.get("arxiv_url")
        if not isinstance(title, str) or not title.strip():
            raise PaperValidationError(f"Paper {index} has no title")
        if not isinstance(arxiv_url, str) or not arxiv_url.strip():
            raise PaperValidationError(f"Paper {index} has no arXiv URL")

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
            if not isinstance(paper.get(field_name), list):
                raise PaperValidationError(
                    f"Paper {index} field '{field_name}' must be a list"
                )

        normalized_id = normalized_arxiv_id(arxiv_url)
        if not normalized_id:
            raise PaperValidationError(f"Paper {index} has an invalid arXiv URL")
        if normalized_id in seen_ids:
            raise PaperValidationError(f"Duplicate arXiv ID: {normalized_id}")
        seen_ids.add(normalized_id)

    return paper_dicts


def merge_paper_collections(
    *collections: Sequence[Any],
) -> List[Dict[str, Any]]:
    """Merge validated paper collections, preferring later metadata."""
    papers_by_id: Dict[str, Dict[str, Any]] = {}
    for collection in collections:
        if not collection:
            continue
        for paper in validate_papers(collection):
            papers_by_id[normalized_arxiv_id(paper["arxiv_url"])] = paper

    if not papers_by_id:
        return []

    merged = sorted(
        papers_by_id.values(),
        key=lambda paper: (
            paper["published_date"],
            normalized_arxiv_id(paper["arxiv_url"]),
        ),
        reverse=True,
    )
    return validate_papers(merged)


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


def build_archive_from_snapshots(data_dir: Path) -> List[Dict[str, Any]]:
    """Build a deduplicated archive from all valid date-named snapshots."""
    snapshots = []
    for path in data_dir.glob("papers_*.json"):
        date_value = snapshot_date(path)
        if date_value is not None:
            snapshots.append((date_value, path))

    archive: List[Dict[str, Any]] = []
    for _, path in sorted(snapshots):
        try:
            papers = load_papers_file(path)
        except (OSError, json.JSONDecodeError, PaperValidationError):
            continue
        archive = merge_paper_collections(archive, papers)
    return archive
