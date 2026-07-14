"""
analysis_writer.py
AIJobAssistant
Version : v1.2.2
"""

from models.job import Job


class AnalysisWriter:

    @staticmethod
    def write(doc, job: Job):

        doc.add_heading(
            "AI ANALYSIS",
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

        add_row("Overall Match", job.match)
        add_row("Total Score", job.total_score)
        add_row("Confidence", job.confidence)
        add_row("Decision", job.decision)

        add_row("Career Score", job.career_score)
        add_row("Role Score", job.role_score)
        add_row("Leadership Score", job.leadership_score)
        add_row("Security Score", job.security_score)
        add_row("Salary Score", job.salary_score)
        add_row("Location Score", job.location_score)
        add_row("Language Score", job.language_score)

        add_row("Strengths", job.strength)
        add_row("Weaknesses", job.weak)
        add_row("Reason", job.reason)
        add_row("Recommendation", job.recommendation)
        add_row("Next Action", job.next_action)

        doc.add_paragraph()