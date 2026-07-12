"""
michaelpage_rule.py
AIJobAssistant
Version : v1.2
"""

from models.job import Job


class MichaelPageRule:

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

        jobs = []

        i = 0

        while i < len(lines):

            position = lines[i]

            if (
                i + 1 < len(lines)
                and (
                    "EUR" in lines[i + 1]
                    or "€" in lines[i + 1]
                    or "Indeterminato" in lines[i + 1]
                    or "Permanent" in lines[i + 1]
                )
            ):

                location = lines[i + 1]

                company = ""

                for j in range(i + 2, min(i + 6, len(lines))):

                    if (
                        "Candidati" in lines[j]
                        or "Apply" in lines[j]
                        or "View Job" in lines[j]
                    ):
                        break

                    if len(lines[j]) > 5:
                        company = lines[j]
                        break

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

                job.portal = "Michael Page"
                job.position = position
                job.location = location
                job.company = company

                jobs.append(job)

            i += 1

        if jobs:
            return jobs

        return [mail]