"""
modules/linkedin/normalizer.py

LinkedIn Text Normalizer
Version : v1.3.1
"""

from __future__ import annotations

import html
import re


SPACE_PATTERN = re.compile(r"\s+")


NOISE_PREFIXES = (
    "based on your",
    "jobs that match",
    "new jobs",
    "your job alert",
)


def normalize_values(values: list[str]) -> list[str]:

    normalized = []

    for value in values:

        value = html.unescape(value)

        value = value.replace("•", "|")
        value = value.replace("·", "|")
        value = value.replace("—", "-")
        value = value.replace("–", "-")

        value = SPACE_PATTERN.sub(" ", value)

        value = value.strip()

        if not value:
            continue

        lower = value.lower()

        if lower.startswith("http"):
            continue

        if "linkedin.com" in lower:
            continue

        if value.startswith("--------------------------------"):
            continue

        if any(lower.startswith(prefix) for prefix in NOISE_PREFIXES):
            continue

        normalized.append(value)

    return normalized