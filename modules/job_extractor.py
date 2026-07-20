"""
modules/job_extractor.py

Job Extractor
Version : v1.2.0
"""

from modules.rules.linkedin_rule import LinkedInRule


class JobExtractor:

    @staticmethod
    def extract(mail):

        if mail is None:
            return None

        if mail.portal == "LinkedIn Job Alerts":
            return LinkedInRule().extract(
                mail,
            )

        return None