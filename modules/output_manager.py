"""
modules/output_manager.py
AIJobAssistant
Version : v2.0.0
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

from config import OUTPUT_DIR
from models.job import Job


class OutputManager:

    def __init__(
        self,
        job: Job,
    ):

        self.job = job

        today = datetime.now().strftime("%Y-%m-%d")
        date = datetime.now().strftime("%Y%m%d")

        company = self._sanitize(job.company)
        position = self._sanitize(job.position)
        country = self._sanitize(job.country)

        self.folder_name = (
            f"{company}_{position}_{country}_{date}"
        )

        self.output_dir = (
            OUTPUT_DIR
            / today
            / self.folder_name
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    @staticmethod
    def _sanitize(
        text: str,
    ) -> str:

        if not text:
            return "Unknown"

        text = re.sub(
            r'[\\/:*?"<>|]',
            "",
            text,
        )

        text = re.sub(
            r"\s+",
            "_",
            text.strip(),
        )

        return text

    # ------------------------------------------------------------------
    # Directory
    # ------------------------------------------------------------------

    def get_output_dir(
        self,
    ) -> Path:

        return self.output_dir

    def get_folder_name(
        self,
    ) -> str:

        return self.folder_name

    # ------------------------------------------------------------------
    # Paths
    # ------------------------------------------------------------------

    def get_jd_html_path(
        self,
    ) -> Path:

        return (
            self.output_dir
            / f"{self.folder_name}.html"
        )

    def get_analysis_path(
        self,
    ) -> Path:

        return (
            self.output_dir
            / "Analysis.md"
        )

    def get_salary_path(
        self,
    ) -> Path:

        return (
            self.output_dir
            / "Salary.txt"
        )

    def get_cv_docx_path(
        self,
    ) -> Path:

        return (
            self.output_dir
            / "Jaeha_Lee_CV.docx"
        )

    def get_cv_pdf_path(
        self,
    ) -> Path:

        return (
            self.output_dir
            / "Jaeha_Lee_CV.pdf"
        )

    def get_cl_docx_path(
        self,
    ) -> Path:

        return (
            self.output_dir
            / "Jaeha_Lee_CL.docx"
        )

    def get_cl_pdf_path(
        self,
    ) -> Path:

        return (
            self.output_dir
            / "Jaeha_Lee_CL.pdf"
        )

    # ------------------------------------------------------------------
    # Save
    # ------------------------------------------------------------------

    def save_job_description(
        self,
        html: str,
    ) -> None:

        if not html:
            raise ValueError(
                "HTML is empty."
            )

        self.get_jd_html_path().write_text(
            html,
            encoding="utf-8",
        )

    def save_salary(
        self,
        salary: str,
    ) -> None:

        self.get_salary_path().write_text(
            salary or "",
            encoding="utf-8",
        )

    def save_analysis(
        self,
    ) -> None:

        job = self.job

        analysis = f"""...

## Company
{job.company}

## Position
{job.position}

## Location
{job.location}

## Salary
{job.salary}

## Match
{job.match}

## Confidence
{job.confidence}

## Strength
{job.strength}

## Weakness
{job.weak}

## Reason
{job.reason}

## Recommendation
{job.recommendation}

## Next Action
{job.next_action}

## Apply URL
{job.apply_url}
"""

        self.get_analysis_path().write_text(
            analysis,
            encoding="utf-8",
        )