"""
dennisgorelik_rule.py
AIJobAssistant
Version : v1.2
"""

from models.job import Job


class DennisGorelikRule:

    @classmethod
    def extract(cls, mail: Job) -> list[Job]:

        text = mail.description or ""

        if not text.strip():
            return [mail]

        lines = []

        for line in text.splitlines():

            line = " ".join(line.split())

            if line:
                lines.append(line)

        position = ""
        company = ""
        location = ""

        for line in lines:

            if (
                " - " in line
                and not company
            ):

                parts = line.split(" - ", 1)

                company = parts[0].strip()

                location = parts[1].strip()

                continue

            if (
                not position
                and len(line) > 5
                and "job" not in line.lower()
                and "postjobfree" not in line.lower()
                and "recommend" not in line.lower()
            ):

                position = line

        if not position:
            return [mail]

        job = Job()

        job.message_id = mail.message_id
        job.thread_id = mail.thread_id
        job.subject = mail.subject
        job.sender = mail.sender
        job.date = mail.date

        job.body = mail.body
        job.description = mail.description
        job.urls = mail.urls
        job.apply_url = mail.apply_url
        job.mail_type = mail.mail_type

        job.portal = "Dennis Gorelik"
        job.position = position
        job.company = company
        job.location = location

        return [job]