"""
modules/report/report_service.py

AIJobAssistant
Version : v2.0.0
"""

from __future__ import annotations

from pathlib import Path

from .report_writer import ReportWriter


class ReportService:
    """Analysis Report Service"""

    @staticmethod
    def create(
        jobs,
        output_dir: Path,
        filename: str = "Analysis_Report.docx",
    ) -> Path:

        output_file = output_dir / filename

        return ReportWriter.write(
            jobs=jobs,
            output_file=output_file,
        )