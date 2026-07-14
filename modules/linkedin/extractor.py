"""
modules/linkedin/extractor.py

LinkedIn Job Extractor
Version : v1.3.0
"""

from __future__ import annotations

from models.job import Job

from modules.linkedin.constants import (
    IGNORE_LINES,
    PORTAL_NAME,
    URL_PATTERN,
    VIEW_JOB_PREFIX,
)
from modules.linkedin.parser import LinkedInParser


class LinkedInExtractor:

    SEARCH_RANGE = 8

    TITLE_KEYWORDS = (
        "manager",
        "lead",
        "director",
        "engineer",
        "architect",
        "consultant",
        "analyst",
        "administrator",
        "specialist",
        "officer",
        "security",
        "cyber",
        "infrastructure",
        "operations",
        "operation",
        "delivery",
        "service",
        "network",
        "cloud",
        "workplace",
        "project",
        "program",
        "governance",
        "risk",
        "compliance",
    )

    LOCATION_KEYWORDS = (
        "remote",
        "hybrid",
        "on-site",
    )

    def __init__(self):

        self.parser = LinkedInParser()

    def extract(self, mail) -> list[Job]:

        lines = self.parser.parse(mail.body)

        jobs = []

        for index, line in enumerate(lines):

            match = URL_PATTERN.match(line)

            if not match:
                continue

            job = Job()

            job.portal = PORTAL_NAME
            job.apply_url = match.group(1)
            job.url = job.apply_url

            values = self._collect_values(
                lines,
                index,
            )

            self._extract_fields(
                job,
                values,
            )

            if job.position:
                jobs.append(job)

        return jobs

    def _collect_values(
        self,
        lines,
        index,
    ) -> list[str]:

        values = []

        i = index - 1

        while i >= 0 and len(values) < self.SEARCH_RANGE:

            value = lines[i].strip()

            if (
                value
                and value not in IGNORE_LINES
                and not value.startswith(VIEW_JOB_PREFIX)
            ):
                values.append(value)

            i -= 1

        values.reverse()

        return values

    @classmethod
    def _extract_fields(
        cls,
        job: Job,
        values: list[str],
    ):

        clean = []

        for value in values:

            value = value.strip()

            if not value:
                continue

            lower = value.lower()

            if lower.startswith("http"):
                continue

            if "linkedin.com" in lower:
                continue

            if value.startswith("--------------------------------"):
                continue

            if value.startswith("Based on your"):
                continue

            if value.startswith("Jobs that match"):
                continue

            if value.startswith("New jobs"):
                continue

            clean.append(value)

        # Position
        for value in clean:

            lower = value.lower()

            if any(keyword in lower for keyword in cls.TITLE_KEYWORDS):
                job.position = value
                break

        # Location
        for value in clean:

            lower = value.lower()

            if (
                "," in value
                or any(keyword in lower for keyword in cls.LOCATION_KEYWORDS)
            ):
                job.location = value
                break

        # Company
        for value in clean:

            if value == job.position:
                continue

            if value == job.location:
                continue

            lower = value.lower()

            if any(keyword in lower for keyword in cls.TITLE_KEYWORDS):
                continue

            job.company = value
            break