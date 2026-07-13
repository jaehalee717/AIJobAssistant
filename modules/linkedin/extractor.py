"""
modules/linkedin/extractor.py

LinkedIn Job Extractor
Version : v1.2.0
"""

from __future__ import annotations

from models.job import Job

from modules.linkedin.constants import (
    IGNORE_LINES,
    PORTAL_NAME,
    URL_PATTERN,
)
from modules.linkedin.parser import LinkedInParser


class LinkedInExtractor:

    def __init__(self):

        self.parser = LinkedInParser()

    def extract(self, mail) -> list[Job]:

        lines = self.parser.parse(mail.body)

        jobs = []

        for index, line in enumerate(lines):

            match = URL_PATTERN.match(line)

            if not match:
                continue

            url = match.group(1)

            values = []

            i = index - 1

            while i >= 0 and len(values) < 3:

                value = lines[i].strip()

                if (
                    value
                    and value not in IGNORE_LINES
                    and not value.startswith("View job:")
                ):
                    values.append(value)

                i -= 1

            if len(values) != 3:
                continue

            job = Job()

            job.portal = PORTAL_NAME

            job.position = values[2]
            job.company = values[1]
            job.location = values[0]

            job.url = url
            job.apply_url = url

            jobs.append(job)

        return jobs