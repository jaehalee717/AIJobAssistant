"""
modules/rules/linkedin_rule.py

LinkedIn Job Alert Rule
Version : v1.1.0
"""

from __future__ import annotations

import re

from bs4 import BeautifulSoup

from models.job import Job


class LinkedInRule:

    IGNORE_LINES = {
        "",
        "Fast growing",
        "Top applicant",
        "Apply with resume & profile",
        "This company is actively hiring",
    }

    URL_PATTERN = re.compile(
        r"^View job:\s*(https://\S+)",
        re.IGNORECASE,
    )

    def extract(self, mail):

        html = mail.body or ""

        soup = BeautifulSoup(html, "html.parser")

        text = soup.get_text("\n", strip=True)

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        jobs = []

        for index, line in enumerate(lines):

            match = self.URL_PATTERN.match(line)

            if not match:
                continue

            url = match.group(1)

            values = []

            i = index - 1

            while i >= 0 and len(values) < 3:

                value = lines[i].strip()

                if (
                    value
                    and value not in self.IGNORE_LINES
                    and not value.startswith("View job:")
                ):
                    values.append(value)

                i -= 1

            if len(values) != 3:
                continue

            job = Job()

            job.portal = "LinkedIn Job Alerts"

            job.position = values[2]
            job.company = values[1]
            job.location = values[0]

            job.url = url
            job.apply_url = url

            jobs.append(job)

        return jobs