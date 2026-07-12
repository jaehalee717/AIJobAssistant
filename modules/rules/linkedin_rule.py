"""
linkedin_rule.py
AIJobAssistant
Version : v2.0
"""

import re

print("★★★★★ NEW LINKEDIN RULE LOADED ★★★★★")

from models.job import Job


class LinkedInRule:

    @classmethod
    def extract(cls, mail: Job) -> list[Job]:

        text = mail.description or ""

        if not text.strip():
            return [mail]

        lines = []

        for line in text.splitlines():

            line = " ".join(line.split()).strip()

            if line:
                lines.append(line)

        jobs = []

        block = []

        def create_job(block_lines):

            if len(block_lines) < 4:
                return None

            position = block_lines[0]
            company = block_lines[1]
            location = block_lines[2]

            invalid = (
                "LinkedIn",
                "View job",
                "See more",
                "Manage job",
                "Unsubscribe",
                "Help",
                "Learn why",
                "You are receiving",
                "Report a bug",
                "This email",
                "new jobs matching",
                "jobs posted by",
                "jobs that mention",
                "connections"
            )

            for word in invalid:

                if position.startswith(word):
                    return None

            if len(position) < 5:
                return None

            job = Job()

            job.message_id = mail.message_id
            job.thread_id = mail.thread_id
            job.subject = mail.subject
            job.sender = mail.sender
            job.date = mail.date

            job.body = mail.body
            job.description = mail.description
            job.urls = mail.urls
            job.mail_type = mail.mail_type

            job.portal = "LinkedIn"

            job.position = position
            job.company = company
            job.location = location

            for line in block_lines:

                if "linkedin.com" in line:
                    m = re.search(r"https?://\S+", line)

                    if m:
                        job.apply_url = m.group(0)
                        break

            return job

        for line in lines:
            print(repr(line))

            if line.startswith("-----"):

                job = create_job(block)
                print("BLOCK RESULT:", job)   # 추가

                if job:
                    jobs.append(job)

                block = []

                continue

            block.append(line)

        job = create_job(block)
        print("LAST BLOCK:", job)   # 추가

        if job:
            jobs.append(job)

        if jobs:
            return jobs

        return [mail]