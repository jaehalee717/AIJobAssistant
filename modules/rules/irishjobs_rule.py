"""
irishjobs_rule.py
AIJobAssistant
Version : v1.2
"""

from models.job import Job


class IrishJobsRule:

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

        for i, line in enumerate(lines):

            lower = line.lower()

            if (
                "technology" in lower
                or "manager" in lower
                or "director" in lower
                or "engineer" in lower
                or "architect" in lower
                or "analyst" in lower
                or "consultant" in lower
                or "lead" in lower
            ):

                if i + 2 >= len(lines):
                    continue

                company = lines[i + 1]

                location = ""

                for j in range(i + 2, min(i + 8, len(lines))):

                    if "," in lines[j] or "dublin" in lines[j].lower():

                        location = lines[j]
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

                job.portal = "IrishJobs"
                job.position = line
                job.company = company
                job.location = location

                jobs.append(job)

                break

        if jobs:
            return jobs

        return [mail]