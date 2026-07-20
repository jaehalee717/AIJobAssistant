"""
modules/linkedin/field_parser.py

LinkedIn Field Parser
Version : v1.4.0
"""

from __future__ import annotations

from modules.linkedin.field_rules import (
    is_company,
    is_location,
    is_position,
    validate,
)


def parse_fields(values: list[str]) -> tuple[str, str, str]:

    if not values:
        return "", "", ""

    # --------------------------------------------------
    # Rule 1
    # Position
    # Company
    # Location
    # --------------------------------------------------

    if len(values) >= 3:

        p = values[-3]
        c = values[-2]
        l = values[-1]

        if (
            is_position(p)
            and is_company(c)
            and is_location(l)
        ):
            return validate(
                p,
                c,
                l,
            )

    # --------------------------------------------------
    # Rule 2
    # Position
    # Location
    # Company
    # --------------------------------------------------

    if len(values) >= 3:

        p = values[-3]
        l = values[-2]
        c = values[-1]

        if (
            is_position(p)
            and is_location(l)
            and is_company(c)
        ):
            return validate(
                p,
                c,
                l,
            )

    # --------------------------------------------------
    # Rule 3
    # Position
    # Company
    # --------------------------------------------------

    if len(values) >= 2:

        p = values[-2]
        c = values[-1]

        if (
            is_position(p)
            and is_company(c)
        ):
            return validate(
                p,
                c,
                "",
            )

    # --------------------------------------------------
    # Rule 4
    # Position
    # Location
    # --------------------------------------------------

    if len(values) >= 2:

        p = values[-2]
        l = values[-1]

        if (
            is_position(p)
            and is_location(l)
        ):
            return validate(
                p,
                "",
                l,
            )

    # --------------------------------------------------
    # Fallback
    # --------------------------------------------------

    position = ""
    company = ""
    location = ""

    for value in values:

        if is_position(value):
            position = value
            break

    for value in values:

        if is_location(value):
            location = value
            break

    for value in values:

        if is_company(value):
            company = value
            break

    return validate(
        position,
        company,
        location,
    )