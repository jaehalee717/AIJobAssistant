"""
modules/rules/linkedin_rule.py

LinkedIn Job Alert Rule
Version : v1.1.0
"""

from __future__ import annotations

from modules.linkedin.extractor import LinkedInExtractor
from modules.linkedin.constants import LINKEDIN_JOB_URL_PREFIXES

class LinkedInRule:

    def __init__(self):

        self.extractor = LinkedInExtractor()

    def extract(
        self, mail,
    ):

        job_url = None

        for url in mail.urls:

            if url.startswith(
                LINKEDIN_JOB_URL_PREFIXES,
            ):
                job_url = url
                break

        if not job_url:
            return None

        return self.extractor.extract(
            job_url,
        )