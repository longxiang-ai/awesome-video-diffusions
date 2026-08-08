"""Boundary-aware text normalization and keyword matching helpers."""

import re
import unicodedata
from typing import Iterable


_NON_WORD_RE = re.compile(r"[^\w]+", re.UNICODE)
_WHITESPACE_RE = re.compile(r"\s+")


def normalize_text(value: str) -> str:
    """Normalize case, Unicode, punctuation, hyphens, and whitespace."""
    normalized = unicodedata.normalize("NFKC", value or "").casefold()
    normalized = _NON_WORD_RE.sub(" ", normalized)
    return _WHITESPACE_RE.sub(" ", normalized).strip()


def contains_phrase(text: str, phrase: str) -> bool:
    """Match a normalized phrase on token boundaries, never as a substring."""
    normalized_text = normalize_text(text)
    normalized_phrase = normalize_text(phrase)
    if not normalized_text or not normalized_phrase:
        return False
    return f" {normalized_phrase} " in f" {normalized_text} "


def contains_any(text: str, phrases: Iterable[str]) -> bool:
    """Return whether text contains at least one boundary-aware phrase."""
    return any(contains_phrase(text, phrase) for phrase in phrases)
