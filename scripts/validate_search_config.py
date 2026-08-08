#!/usr/bin/env python3
"""Validate fallback and effective arXiv search configuration."""

import json
import re
import sys
from pathlib import Path


KEYWORD_SCOPES = ("both_abstract_and_title", "abstract_only", "title_only")
RELEVANCE_FIELDS = (
    "strong_phrases",
    "conditional_title_phrases",
    "excluded_title_phrases",
    "video_evidence_phrases",
    "generation_evidence_phrases",
)
DOMAIN_PATTERN = re.compile(r"[a-z-]+\.[A-Za-z-]+")


class ConfigValidationError(ValueError):
    """Raised when a tracked search configuration is invalid."""


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ConfigValidationError(f"Unable to load {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ConfigValidationError(f"{path} must contain a JSON object")
    return value


def validate_phrase_list(value, label: str, allow_empty: bool = False) -> list[str]:
    if not isinstance(value, list) or (not value and not allow_empty):
        qualifier = "an array" if allow_empty else "a non-empty array"
        raise ConfigValidationError(f"{label} must be {qualifier}")
    phrases = []
    seen = set()
    for index, phrase in enumerate(value):
        if not isinstance(phrase, str) or not phrase.strip():
            raise ConfigValidationError(f"{label}[{index}] must be a non-empty string")
        phrase = phrase.strip()
        if '"' in phrase:
            raise ConfigValidationError(f'{label}[{index}] must not contain "')
        key = phrase.casefold()
        if key in seen:
            raise ConfigValidationError(f"Duplicate phrase in {label}: {phrase}")
        seen.add(key)
        phrases.append(phrase)
    return phrases


def validate_keywords(
    value, label: str, allow_all_empty: bool = False
) -> dict[str, list[str]]:
    if not isinstance(value, dict):
        raise ConfigValidationError(f"{label} must be a JSON object")
    result = {
        scope: validate_phrase_list(
            value.get(scope), f"{label}.{scope}", allow_empty=True
        )
        for scope in KEYWORD_SCOPES
    }
    if not allow_all_empty and not any(result.values()):
        raise ConfigValidationError(f"{label} must contain at least one phrase")
    owners = {}
    for scope, phrases in result.items():
        for phrase in phrases:
            key = phrase.casefold()
            if key in owners:
                raise ConfigValidationError(
                    f"Phrase {phrase!r} appears in both {owners[key]} and {scope}"
                )
            owners[key] = scope
    return result


def validate_relevance(value, label: str) -> None:
    if not isinstance(value, dict):
        raise ConfigValidationError(f"{label} must be a JSON object")
    for field in RELEVANCE_FIELDS:
        validate_phrase_list(value.get(field), f"{label}.{field}")


def validate_config(project_root: Path = Path(".")) -> bool:
    data_dir = Path(project_root) / "data"
    fallback_path = data_dir / "search_config.json"
    user_path = data_dir / "user_config.json"
    fallback = load_json(fallback_path)
    user = load_json(user_path)

    fallback_keywords = validate_keywords(
        fallback.get("search_config"), "search_config.search_config"
    )
    validate_relevance(
        fallback.get("relevance_filter"), "search_config.relevance_filter"
    )

    search = user.get("search")
    if not isinstance(search, dict):
        raise ConfigValidationError("user_config.search must be a JSON object")
    user_keywords = validate_keywords(
        search.get("keywords"),
        "user_config.search.keywords",
        allow_all_empty=True,
    )
    effective_keywords = user_keywords if any(user_keywords.values()) else fallback_keywords

    user_relevance = search.get("relevance_filter")
    if user_relevance is not None:
        validate_relevance(
            user_relevance, "user_config.search.relevance_filter"
        )
    effective_relevance = user_relevance or fallback.get("relevance_filter")
    validate_relevance(effective_relevance, "effective.relevance_filter")

    domains = search.get("domains")
    if not isinstance(domains, list):
        raise ConfigValidationError("user_config.search.domains must be an array")
    if any(not isinstance(domain, str) or not DOMAIN_PATTERN.fullmatch(domain)
           for domain in domains):
        raise ConfigValidationError("user_config.search.domains contains an invalid value")
    if len(set(domains)) != len(domains):
        raise ConfigValidationError("user_config.search.domains contains duplicates")

    max_results = search.get("max_results")
    if not isinstance(max_results, int) or not 1 <= max_results <= 5000:
        raise ConfigValidationError("user_config.search.max_results must be 1..5000")

    time_range = search.get("time_range")
    if not isinstance(time_range, dict) or time_range.get("mode") not in {
        "relative", "absolute", "none"
    }:
        raise ConfigValidationError("user_config.search.time_range is invalid")

    print(f"[OK] Valid fallback config: {fallback_path}")
    print(f"[OK] Valid effective config: {user_path}")
    print(
        f"[OK] Effective search: {sum(len(effective_keywords[scope]) for scope in KEYWORD_SCOPES)} "
        f"phrases, {len(domains)} domains, max_results={max_results}"
    )
    return True


if __name__ == "__main__":
    try:
        validate_config()
    except ConfigValidationError as exc:
        print(f"[ERROR] Search configuration is invalid: {exc}")
        sys.exit(1)
