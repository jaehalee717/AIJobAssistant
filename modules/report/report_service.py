"""
modules/report/report_service.py

AIJobAssistant
Version : v4.0.0
"""

from __future__ import annotations

from pathlib import Path

from .report_writer import ReportWriter


class ReportService:
    """Analysis Report Service"""

    DEFAULT_FILENAME = "Analysis_Report.docx"

    @classmethod
    def create(
        cls,
        jobs,
        output_dir: Path,
        filename: str | None = None,
    ) -> Path:

        output_file = output_dir / (
            filename or cls.DEFAULT_FILENAME
        )

        return ReportWriter.write(
            jobs=jobs,
            output_file=output_file,
        )