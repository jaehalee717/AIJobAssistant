"""
modules/linkedin/jd_extractor.py

LinkedIn Job Description Extractor
AIJobAssistant v1.5.1
"""

from __future__ import annotations

from pathlib import Path

from modules.linkedin.parser import LinkedInParser


class LinkedInJDExtractor:

    def __init__(
        self,
        output_dir: Path | None = None,
    ):

        self.output_dir = output_dir

    def extract_from_html(
        self,
        html: str,
    ) -> dict:

        if not html:
            return {
                "company": "",
                "position": "",
                "location": "",
                "description": "",
            }

        return LinkedInParser.extract_jd(html)

    def save_html(
        self,
        html: str,
        path: Path,
    ):

        path.write_text(
            html,
            encoding="utf-8",
        )

    def save_text(
        self,
        text: str,
        path: Path,
    ):

        path.write_text(
            text,
            encoding="utf-8",
        )

    def save_job(
        self,
        job: dict,
        path: Path,
    ):

        lines = [
            f"Company    : {job.get('company', '')}",
            f"Position   : {job.get('position', '')}",
            f"Location   : {job.get('location', '')}",
            "",
            "=" * 80,
            "JOB DESCRIPTION",
            "=" * 80,
            "",
            job.get("description", ""),
        ]

        path.write_text(
            "\n".join(lines),
            encoding="utf-8",
        )