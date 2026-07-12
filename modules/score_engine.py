"""
score_engine.py
AIJobAssistant
Version : v1.0.1
"""

from models.job import Job


class ScoreEngine:

    CAREER_KEYWORDS = [
        "it",
        "information technology",
        "infrastructure",
        "cyber",
        "security",
        "information security",
        "cloud",
        "network",
        "server",
        "helpdesk",
        "erp",
        "sap",
        "governance",
        "risk",
        "grc",
    ]

    LEVEL_KEYWORDS = [
        "manager",
        "head",
        "director",
        "lead",
        "senior manager",
        "it manager",
        "head of it",
        "it director",
        "information security manager",
        "cyber security manager",
    ]

    @classmethod
    def evaluate(cls, job: Job) -> Job:

        score = 0

        strengths = []
        weaknesses = []

        text = " ".join([
            job.subject,
            job.position,
            job.company,
            job.location,
            job.description,
        ]).lower()

        # Career (35)

        if any(k in text for k in cls.CAREER_KEYWORDS):

            score += 35
            strengths.append("Career Match")

        else:

            weaknesses.append("Career")

        # Level (30)

        if any(k in text for k in cls.LEVEL_KEYWORDS):

            score += 30
            strengths.append("Job Level")

        else:

            weaknesses.append("Job Level")

        # English (10)

        if "english" in text:

            score += 10
            strengths.append("English")

        # Salary (10)

        if any(x in text for x in [
            "€",
            "eur",
            "$",
            "usd",
            "salary",
        ]):

            score += 10
            strengths.append("Salary")

        # Visa (15)

        score += 15
        strengths.append("EU Work Authorization")

        job.match = score

        if score >= 80:

            job.decision = "APPLY"
            job.confidence = "High"

        elif score >= 60:

            job.decision = "REVIEW"
            job.confidence = "Medium"

        else:

            job.decision = "SKIP"
            job.confidence = "Low"

        job.strength = ", ".join(strengths)
        job.weak = ", ".join(weaknesses)

        if job.decision == "APPLY":
            job.reason = "Strong match."

        elif job.decision == "REVIEW":
            job.reason = "Needs manual review."

        else:
            job.reason = "Low relevance."

        return job