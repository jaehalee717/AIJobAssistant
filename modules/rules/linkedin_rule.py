"""
modules/rules/linkedin_rule.py

LinkedIn Job Alert Rule
Version : v1.1.0
"""

from __future__ import annotations

from modules.linkedin.extractor import LinkedInExtractor

class LinkedInRule:

    def __init__(self):

        self.extractor = LinkedInExtractor()

    def extract(self, mail):

        return self.extractor.extract(mail)