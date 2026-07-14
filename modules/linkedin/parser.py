"""
modules/linkedin/parser.py

LinkedIn HTML Parser
Version : v1.2.1
"""

from __future__ import annotations

from bs4 import BeautifulSoup


class LinkedInParser:

    IGNORE_PREFIXES = (
        "Manage preferences",
        "Unsubscribe",
        "Help",
        "Privacy",
        "Terms",
        "LinkedIn Corporation",
    )

    @classmethod
    def parse(cls, html: str) -> list[str]:

        soup = BeautifulSoup(
            html or "",
            "html.parser",
        )

        text = soup.get_text(
            "\n",
            strip=True,
        )

        lines = []
        seen = set()

        for line in text.splitlines():

            line = " ".join(line.split())

            if not line:
                continue

            if any(
                line.startswith(prefix)
                for prefix in cls.IGNORE_PREFIXES
            ):
                continue

            if line in seen:
                continue

            seen.add(line)
            lines.append(line)

        return lines