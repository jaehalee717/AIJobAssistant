"""
modules/output_manager.py
AIJobAssistant
Version : v1.5.0
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

from config import OUTPUT_DIR
from models.job import Job


class OutputManager:

    def __init__(self, job: Job):

        self.job = job

        today = datetime.now().strftime("%Y-%m-%d")
        date = datetime.now().strftime("%Y%m%d")

        company = self._sanitize(job.company)
        position = self._sanitize(job.position)
        country = self._sanitize(job.country)

        folder = f"{company}_{position}_{country}_{date}"

        self.output_dir = OUTPUT_DIR / today / folder
        self.output_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _sanitize(text: str) -> str:

        if not text:
            return "Unknown"

        text = re.sub(r'[\\/:*?"<>|]', "", text)
        text = re.sub(r"\s+", "_", text.strip())

        return text

    def get_cv_docx_path(self) -> Path:
        return self.output_dir / "Jaeha_Lee_CV.docx"

    def get_cv_pdf_path(self) -> Path:
        return self.output_dir / "Jaeha_Lee_CV.pdf"

    def get_cl_docx_path(self) -> Path:
        return self.output_dir / "Jaeha_Lee_CL.docx"

    def get_cl_pdf_path(self) -> Path:
        return self.output_dir / "Jaeha_Lee_CL.pdf"

    def get_jd_html_path(self) -> Path:
        return self.output_dir / "Job_Description.html"

    def get_salary_path(self) -> Path:
        return self.output_dir / "Salary.txt"

    def get_report_path(self) -> Path:
        return self.output_dir / "Report.md"

    def save_job_description(self, html: str) -> None:

        self.get_jd_html_path().write_text(
            html,
            encoding="utf-8",
        )

    def save_salary(self, salary: str) -> None:

        self.get_salary_path().write_text(
            salary or "",
            encoding="utf-8",
        )

    def save_report(self, job: Job) -> None:

        report = f"""# Job Report

Company: {job.company}
Position: {job.position}
Location: {job.location}
Salary: {job.salary}

Match: {job.match}
Confidence: {job.confidence}

Strength:
{job.strength}

Weak:
{job.weak}

Reason:
{job.reason}

Recommendation:
{job.recommendation}

Next Action:
{job.next_action}

Apply URL:
{job.apply_url}
"""

        self.get_report_path().write_text(
            report,
            encoding="utf-8",
        )