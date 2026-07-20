"""
modules/report/summary_writer.py

AIJobAssistant
Version : v2.0.0
"""

from __future__ import annotations

from docx.document import Document


class SummaryWriter:
    """분석 요약 작성."""

    @staticmethod
    def write(
        document: Document,
        jobs,
    ) -> None:

        total = len(jobs)

        recommended = sum(
            1
            for job in jobs
            if getattr(job, "recommendation", "").upper()
            in ("APPLY", "RECOMMENDED", "YES")
        )

        document.add_heading(
            "Summary",
            level=1,
        )

        document.add_paragraph(
            f"Total Jobs : {total}"
        )

        document.add_paragraph(
            f"Recommended : {recommended}"
        )

        document.add_paragraph(
            f"Not Recommended : {total - recommended}"
        )