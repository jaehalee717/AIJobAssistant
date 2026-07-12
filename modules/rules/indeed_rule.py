"""
indeed_rule.py
AIJobAssistant
Version : v1.2
"""

import re

from models.job import Job


class IndeedRule:

    LOCATION_PATTERN = re.compile(
        r"(Germany|Deutschland|Berlin|Hamburg|Munich|München|Frankfurt|Bremen|Köln|Cologne)",
        re.IGNORECASE,
    )

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
                and len(position) > 5
                and not position.lower().startswith("indeed")
            ):

                company = lines[i + 1]

                location = ""

                for j in range(i + 2, min(i + 6, len(lines))):

                    if cls.LOCATION_PATTERN.search(lines[j]):

                        location = lines[j]
                        break

                if location:

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

                    job.portal = "Indeed"
                    job.position = position
                    job.company = company
                    job.location = location

                    jobs.append(job)

            i += 1

        if jobs:
            return jobs

        return [mail]