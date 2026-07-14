"""
summary_writer.py
AIJobAssistant
Version : v1.2.2
"""

from docx.shared import Pt

from models.job import Job
from utils.word_helper import add_hyperlink


class SummaryWriter:

    @staticmethod
    def write(doc, job: Job):

        doc.add_heading(
            "JOB SUMMARY",
            level=3,
        )

        table = doc.add_table(
            rows=0,
            cols=2,
        )

        table.style = "Table Grid"

        def add_row(name: str, value):

            cells = table.add_row().cells
            cells[0].text = name
            cells[1].text = "" if value is None else str(value)

        add_row("Company", job.company)
        add_row("Position", job.position)
        add_row("Portal", job.portal)
        add_row("Location", job.location)
        add_row("Employment", job.employment_type)
        add_row("Remote", job.remote)
        add_row("Salary", job.salary)

        cells = table.add_row().cells
        cells[0].text = "Apply URL"

        if job.apply_url:

            add_hyperlink(
                cells[1].paragraphs[0],
                "Open Job Posting",
                job.apply_url,
            )

        doc.add_paragraph()