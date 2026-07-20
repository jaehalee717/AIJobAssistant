"""
modules/report/analysis_writer.py

AIJobAssistant
Version : v2.0.0
"""

from __future__ import annotations

from docx.document import Document

from .table_builder import TableBuilder


class AnalysisWriter:
    """1차 분석 결과 작성."""

    @staticmethod
    def write(
        document: Document,
        jobs,
    ) -> None:

        document.add_heading(
            "Job Analysis",
            level=1,
        )

        headers, rows = TableBuilder.build(
            jobs
        )

        table = document.add_table(
            rows=1,
            cols=len(headers),
        )

        table.style = "Table Grid"

        for col, header in enumerate(headers):
            table.rows[0].cells[col].text = header

        for row in rows:
            cells = table.add_row().cells

            for col, value in enumerate(row):
                cells[col].text = value