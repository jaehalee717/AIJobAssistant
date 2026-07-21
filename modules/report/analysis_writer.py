"""
modules/report/analysis_writer.py

AIJobAssistant
Version : v2.1.0
"""

from __future__ import annotations

from docx.document import Document


class AnalysisWriter:

    @staticmethod
    def write(
        document: Document,
        job,
    ) -> None:

        document.add_heading(
            "Analysis",
            level=3,
        )

        document.add_paragraph(
            f"Reason : {job.reason}"
        )