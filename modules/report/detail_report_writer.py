"""
modules/report/detail_report_writer.py

AIJobAssistant
Version : v2.2.0
"""

from __future__ import annotations

from pathlib import Path

from docx import Document

from .detail_writer import DetailWriter
from .summary_writer import SummaryWriter


class DetailReportWriter:
    """Detail Analysis Report 생성."""

    @staticmethod
    def write(
        jobs,
        output_file: Path,
    ) -> Path:

        document = Document()

        document.add_heading(
            "Detail AIJobAssistant Report",
            level=0,
        )

        SummaryWriter.write(
            document,
            jobs,
        )

        DetailWriter.write(
            document,
            jobs,
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        document.save(
            output_file,
        )

        return output_file