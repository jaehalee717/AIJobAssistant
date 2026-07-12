"""
job_extractor.py
AIJobAssistant
Version : v1.1.0

One Mail -> Multiple Jobs
"""

import re

from models.job import Job

from modules.rules.generic_rule import GenericRule
from modules.rules.linkedin_rule import LinkedInRule
from modules.rules.irishjobs_rule import IrishJobsRule
from modules.rules.indeed_rule import IndeedRule
from modules.rules.michaelpage_rule import MichaelPageRule
from modules.rules.pageexecutive_rule import PageExecutiveRule
from modules.rules.dennisgorelik_rule import DennisGorelikRule
from modules.rules.gulftalent_rule import GulfTalentRule


class JobExtractor:

    @classmethod
    def extract(cls, mail: Job) -> list[Job]:

        portal = getattr(mail, "portal", "Other")

        if portal == "LinkedIn":
            return LinkedInRule.extract(mail)

        if portal == "IrishJobs":
            return IrishJobsRule.extract(mail)

        if portal == "Indeed":
            return IndeedRule.extract(mail)

        if portal == "Michael Page":
            return MichaelPageRule.extract(mail)

        if portal == "Page Executive":
            return PageExecutiveRule.extract(mail)

        if portal == "Dennis Gorelik":
            return DennisGorelikRule.extract(mail)

        if portal == "GulfTalent":
            return GulfTalentRule.extract(mail)

        return GenericRule.extract(mail)