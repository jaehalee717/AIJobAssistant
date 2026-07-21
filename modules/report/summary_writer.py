"""
modules/report/summary_writer.py

AIJobAssistant
Version : v2.2.1
"""

from __future__ import annotations

from docx.document import Document


class SummaryWriter:

    @staticmethod
    def write(
        document: Document,
        jobs,
    ) -> None:

        document.add_heading(
            "Summary",
            level=3,
        )

        for job in jobs:

            document.add_paragraph(
                f"Company : {job.company}"
            )

            document.add_paragraph(
                f"Position : {job.position}"
            )

            document.add_paragraph(
                f"Location : {job.location}"
            )

            document.add_paragraph(
                f"Salary : {job.salary}"
            )

            document.add_paragraph(
                f"Recommendation : {job.decision}"
            )

            document.add_paragraph(
                f"Score : {job.match}"
            )

            document.add_paragraph()