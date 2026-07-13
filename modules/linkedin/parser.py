"""
modules/linkedin/parser.py

LinkedIn HTML Parser
Version : v1.2.0
"""

from __future__ import annotations

from bs4 import BeautifulSoup


class LinkedInParser:

    def parse(self, html: str) -> list[str]:

        soup = BeautifulSoup(html or "", "html.parser")

        text = soup.get_text("\n", strip=True)

        return [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]