"""
hard_rule.py
AIJobAssistant
Version : v1.3.1
"""

from models.job import Job


class HardRule:

    UNSUPPORTED_LANGUAGE = [
        "german required",
        "german fluent",
        "french required",
        "french fluent",
        "dutch required",
        "polish required",
    ]

    UNSUPPORTED_SKILL = [
        "kubernetes expert",
        "terraform expert",
        "aws security specialty",
        "principal devsecops",
        "staff software engineer",
        "machine learning scientist",
    ]

    @classmethod
    def evaluate(cls, job: Job) -> tuple[bool, str]:

        text = " ".join([
            job.subject,
            job.position,
            job.company,
            job.location,
            job.description,
        ]).lower()

        # Mandatory Language

        if any(x in text for x in cls.UNSUPPORTED_LANGUAGE):

            return (
                False,
                "Mandatory language requirement is not currently supported.",
            )

        # Unrealistic Skill Gap

        if any(x in text for x in cls.UNSUPPORTED_SKILL):

            return (
                False,
                "Current experience is significantly different from the required role.",
            )

        return True, ""