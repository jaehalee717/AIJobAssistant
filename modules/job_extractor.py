"""
job_extractor.py
AIJobAssistant
Version : v1.1.0

One Mail -> Multiple Jobs
"""

import re

from models.job import Job


class JobExtractor:

    POSITION_WORDS = [
        "manager",
        "director",
        "head",
        "lead",
        "engineer",
        "architect",
        "administrator",
        "analyst",
        "consultant",
        "developer",
        "specialist",
        "officer",
        "security",
        "cyber",
        "cloud",
        "network",
        "infrastructure",
        "service delivery",
        "operations",
        "platform",
        "grc",
        "risk",
        "technology",
        "innovation",
        "automation",
        "testing",
        "frontend",
        "command centre",
        "command center",
        "ai",
    ]

    COMPANY_SKIP = [
        "easy apply",
        "actively recruiting",
        "explore",
        "view more jobs",
        "see all jobs",
        "manage",
        "unsubscribe",
        "privacy",
        "linkedin",
        "irishjobs",
        "aia",
    ]

    LOCATION_PATTERN = re.compile(
        r"\((Hybrid|Remote|On-site|Onsite)\)",
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

            if not line:
                continue

            lines.append(line)

        jobs = []

        current = None

        for line in lines:

            lower = line.lower()

            if any(word in lower for word in cls.POSITION_WORDS):

                if current:
                    jobs.append(current)

                current = Job()

                current.message_id = mail.message_id
                current.thread_id = mail.thread_id
                current.subject = mail.subject
                current.sender = mail.sender
                current.date = mail.date

                current.body = mail.body
                current.description = mail.description
                current.urls = mail.urls
                current.apply_url = mail.apply_url
                current.mail_type = mail.mail_type

                current.position = line

                continue

            if current is None:
                continue

            if not current.company:

                if len(line) < 60:

                    if not any(x in lower for x in cls.COMPANY_SKIP):

                        current.company = line
                        continue

            if not current.location:

                m = cls.LOCATION_PATTERN.search(line)

                if m:

                    current.location = line

        if current:
            jobs.append(current)

        if not jobs:
            jobs.append(mail)

        return jobs