"""
modules/linkedin/parser.py

LinkedIn HTML Parser
Version : v1.3.1
"""

from __future__ import annotations

import re

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

    END_MARKERS = (
        "People also viewed",
        "Jobs you may like",
        "Recommended for you",
        "Report this job",
        "Show more",
        "Set alert",
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

    @classmethod
    def extract_jd(cls, html: str) -> dict:

        soup = BeautifulSoup(
            html or "",
            "html.parser",
        )

        text = soup.get_text(
            "\n",
            strip=True,
        )

        return {
            "company": cls._extract_company(soup),
            "position": cls._extract_position(soup),
            "location": cls._extract_location(soup),
            "description": cls._extract_description(text),
        }

    @classmethod
    def _extract_company(cls, soup: BeautifulSoup) -> str:

        tag = soup.select_one(
            'a[href*="/company/"]'
        )

        if tag:
            return " ".join(tag.get_text(" ", strip=True).split())

        return ""

    @classmethod
    def _extract_position(cls, soup: BeautifulSoup) -> str:

        # 1. h1
        h1 = soup.find("h1")

        if h1:
            text = " ".join(
                h1.get_text(" ", strip=True).split()
            )

            if text:
                return text

        # 2. Open Graph
        meta = soup.find(
            "meta",
            attrs={
                "property": "og:title",
            },
        )

        if meta:

            text = meta.get(
                "content",
                "",
            ).strip()

            if text:

                text = text.replace(
                    " | LinkedIn",
                    "",
                )

                return text

        # 3. HTML <title>
        if soup.title:

            title = soup.title.get_text(
                " ",
                strip=True,
            )

            title = title.replace(
                "| LinkedIn",
                "",
            )

            separators = (
                " - ",
                " | ",
                " at ",
            )

            for separator in separators:

                if separator in title:

                    title = title.split(
                        separator
                    )[0].strip()

            if title:
                return title

        # 4. Description 첫 줄 이용
        text = cls._extract_description(
            soup.get_text(
                "\n",
                strip=True,
            )
        )

        if text:

            lines = [
                line.strip()
                for line in text.splitlines()
                if line.strip()
            ]

            if len(lines) >= 2:
                return lines[1]

        return ""

    @classmethod
    def _extract_location(cls, soup: BeautifulSoup) -> str:

        patterns = (
            "Remote",
            "Hybrid",
            "On-site",
        )

        for span in soup.find_all("span"):

            text = " ".join(
                span.get_text(" ", strip=True).split()
            )

            if not text:
                continue

            if len(text) > 100:
                continue

            if "," in text:
                return text

            if any(
                p.lower() in text.lower()
                for p in patterns
            ):
                return text

        return ""

    @classmethod
    def _extract_description(cls, text: str) -> str:

        match = re.search(
            r"About the job",
            text,
            re.IGNORECASE,
        )

        if not match:
            return ""

        description = text[match.start():]

        end = len(description)

        for marker in cls.END_MARKERS:

            idx = description.find(marker)

            if idx != -1:
                end = min(end, idx)

        description = description[:end]

        description = re.sub(
            r"\n{3,}",
            "\n\n",
            description,
        )

        return description.strip()