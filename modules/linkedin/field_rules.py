"""
modules/linkedin/field_rules.py

LinkedIn Field Rules
Version : v1.4.0
"""

from __future__ import annotations

from modules.linkedin.field_keywords import (
    COUNTRY_WORDS,
    LOCATION_KEYWORDS,
    NOISE_WORDS,
    TITLE_KEYWORDS,
)


def is_position(value: str) -> bool:

    lower = value.lower()

    return any(keyword in lower for keyword in TITLE_KEYWORDS)


def is_location(value: str) -> bool:

    lower = value.lower()

    if "," in value:
        return True

    if any(country in lower for country in COUNTRY_WORDS):
        return True

    return any(keyword in lower for keyword in LOCATION_KEYWORDS)


def is_noise(value: str) -> bool:

    lower = value.lower()

    return any(word in lower for word in NOISE_WORDS)


def is_company(value: str) -> bool:

    if not value:
        return False

    if is_position(value):
        return False

    if is_location(value):
        return False

    if is_noise(value):
        return False

    if value.isdigit():
        return False

    return 2 <= len(value) <= 80


def validate(
    position: str,
    company: str,
    location: str,
) -> tuple[str, str, str]:

    position = position.strip()
    company = company.strip()
    location = location.strip()

    if position == company:
        company = ""

    if position == location:
        location = ""

    if company == location:
        company = ""

    if position and company.startswith(position):
        company = ""

    if position and location.startswith(position):
        location = ""

    return (
        position,
        company,
        location,
    )