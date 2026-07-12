"""
report_generator.py
AIJobAssistant
Version : v1.1.0
"""

import re
from pathlib import Path
from datetime import datetime

from docx import Document
from docx.shared import Pt

from models.job import Job


class ReportGenerator:

    def __init__(self, report_folder: str):

        self.report_folder = Path(report_folder)
        self.report_folder.mkdir(
            parents=True,
            exist_ok=True,
        )

    @staticmethod
    def safe_filename(text: str) -> str:

        if not text:
            return "Unknown"

        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r'[\\/:*?"<>|]', "_", text)
        text = re.sub(r"\s+", " ", text).strip()

        if len(text) > 60:
            text = text[:60]

        return text or "Unknown"

    def generate(self, job: Job) -> str:

        doc = Document()

        title = doc.add_heading(
            "AI Job Assistant Report",
            level=1,
        )

        title.runs[0].font.size = Pt(18)

        doc.add_paragraph(
            f"Generated : {datetime.now():%Y-%m-%d %H:%M:%S}"
        )

        doc.add_paragraph()

        doc.add_heading("Job Information", level=2)

        table = doc.add_table(rows=0, cols=2)
        table.style = "Table Grid"

        def add_row(name, value):

            cells = table.add_row().cells
            cells[0].text = name
            cells[1].text = value or ""

        add_row("Company", job.company)
        add_row("Position", job.position)
        add_row("Location", job.location)
        add_row("Apply URL", job.apply_url)
        add_row("Mail Type", job.mail_type)

        doc.add_paragraph()

        doc.add_heading("Evaluation", level=2)

        table = doc.add_table(rows=0, cols=2)
        table.style = "Table Grid"

        add = lambda n, v: (
            (lambda c: (
                setattr(c[0], "text", n),
                setattr(c[1], "text", str(v))
            ))(table.add_row().cells)
        )

        add("Match", job.match)
        add("Decision", job.decision)
        add("Confidence", job.confidence)
        add("Strength", job.strength)
        add("Weak", job.weak)
        add("Reason", job.reason)

        doc.add_paragraph()

        doc.add_heading("Mail", level=2)

        body = job.description or job.body or ""

        if len(body) > 8000:
            body = body[:8000]

        doc.add_paragraph(body)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        company = self.safe_filename(job.company)
        position = self.safe_filename(job.position)

        filename = (
            f"{timestamp}"
            f"_{company}"
            f"_{position}.docx"
        )

        filepath = self.report_folder / filename

        doc.save(filepath)

        return str(filepath)