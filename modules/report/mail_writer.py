"""
mail_writer.py
AIJobAssistant
Version : v1.2.2
"""

from models.job import Job


class MailWriter:

    MAX_BODY_LENGTH = 8000

    @staticmethod
    def write(doc, job: Job):

        doc.add_heading(
            "ORIGINAL MAIL",
            level=3,
        )

        body = job.description or job.body or ""

        if len(body) > MailWriter.MAX_BODY_LENGTH:
            body = body[:MailWriter.MAX_BODY_LENGTH]

        doc.add_paragraph(body)

        doc.add_page_break()