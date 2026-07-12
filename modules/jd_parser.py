"""
jd_parser.py
AIJobAssistant
Version : v1.0.0
"""

import re

from models.job import Job


class JDParser:

    POSITION_KEYWORDS = [
        "manager",
        "director",
        "head",
        "lead",
        "engineer",
        "architect",
        "specialist",
        "consultant",
        "administrator",
        "analyst",
        "developer",
        "officer",
        "security",
        "cyber",
        "infrastructure",
        "cloud",
        "network",
        "it ",
        "information technology",
    ]

    COMPANY_SKIP = [
        "apply",
        "linkedin",
        "job",
        "jobs",
        "career",
        "careers",
        "salary",
        "location",
        "description",
        "responsibilities",
        "requirements",
    ]

    LOCATION_PATTERN = re.compile(
        r"(Remote|Hybrid|On[- ]?site|[A-Za-zÀ-ÿ .'-]+,\s*[A-Za-zÀ-ÿ .'-]+)",
        re.IGNORECASE,
    )

    @classmethod
    def parse(cls, job: Job) -> Job:

        text = (job.description or "").strip()

        if not text:
            return job

        # URL
        m = re.search(r"https?://\S+", text)

        if m:
            job.url = m.group(0)

        lines = []

        for line in text.splitlines():

            line = " ".join(line.split())

            if not line:
                continue

            if len(line) < 3:
                continue

            if line.lower().startswith("http"):
                continue

            lines.append(line)

        # Position
        if not job.position:

            for line in lines:

                lower = line.lower()

                if any(k in lower for k in cls.POSITION_KEYWORDS):

                    job.position = line
                    break

        # Company
        if not job.company:

            for line in lines:

                if line == job.position:
                    continue

                if len(line) > 60:
                    continue

                lower = line.lower()

                if any(k in lower for k in cls.COMPANY_SKIP):
                    continue

                if re.search(r"\d{4}", line):
                    continue

                job.company = line
                break

        # Location
        if not job.location:

            for line in lines:

                m = cls.LOCATION_PATTERN.search(line)

                if m:
                    job.location = m.group(0)
                    break

        job.description = "\n".join(lines)

        return job