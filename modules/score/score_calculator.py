"""
score_calculator.py
AIJobAssistant
Version : v1.3.1
"""

from models.job import Job


class ScoreCalculator:

    PERFORMANCE = [
        "it",
        "information technology",
        "it infrastructure",
        "infrastructure",
        "it operations",
        "service delivery",
        "information security",
        "cyber security",
        "cybersecurity",
        "grc",
        "risk",
        "governance",
        "iso 27001",
        "manufacturing",
        "erp",
        "sap",
        "network",
        "server",
        "cloud",
    ]

    LEADERSHIP = [
        "manager",
        "head",
        "lead",
        "specialist",
        "principal",
        "architect",
        "consultant",
    ]

    LANGUAGE = [
        "english",
        "spanish",
        "portuguese",
        "korean",
    ]

    @classmethod
    def calculate(cls, job: Job) -> Job:

        text = " ".join([
            job.subject,
            job.position,
            job.company,
            job.location,
            job.description,
        ]).lower()

        # 1. Job Performance Fit (40)

        job.career_score = (
            40
            if any(x in text for x in cls.PERFORMANCE)
            else 0
        )

        # 2. Hiring Probability (20)

        hiring = 0

        if job.company:
            hiring += 5

        if job.location:
            hiring += 5

        if job.apply_url:
            hiring += 5

        if job.description:
            hiring += 5

        job.role_score = hiring

        # 3. Leadership / Seniority (10)

        job.leadership_score = (
            10
            if any(x in text for x in cls.LEADERSHIP)
            else 0
        )

        # 4. Information Security (10)

        job.security_score = (
            10
            if any(
                x in text
                for x in [
                    "security",
                    "cyber",
                    "grc",
                    "iso 27001",
                ]
            )
            else 0
        )

        # 5. Salary (10)

        job.salary_score = (
            10
            if any(
                x in text
                for x in [
                    "salary",
                    "eur",
                    "€",
                    "usd",
                    "$",
                ]
            )
            else 0
        )

        # 6. Country / Location (5)

        job.location_score = (
            5 if job.location else 0
        )

        # 7. Language (5)

        job.language_score = (
            5
            if any(x in text for x in cls.LANGUAGE)
            else 0
        )

        job.total_score = (
            job.career_score +
            job.role_score +
            job.leadership_score +
            job.security_score +
            job.salary_score +
            job.location_score +
            job.language_score
        )

        job.match = job.total_score

        return job