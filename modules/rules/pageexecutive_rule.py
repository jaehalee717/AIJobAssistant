"""
pageexecutive_rule.py
AIJobAssistant
Version : v1.2
"""

from models.job import Job


class PageExecutiveRule:

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
                and "," in lines[i + 1]
                and (
                    "Permanent" in lines[i + 1]
                    or "Temporary" in lines[i + 1]
                )
            ):

                location = lines[i + 1]

                company = "Page Executive"

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

                job.portal = "Page Executive"
                job.position = position
                job.company = company
                job.location = location

                jobs.append(job)

            i += 1

        if jobs:
            return jobs

        return [mail]