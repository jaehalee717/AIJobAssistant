"""
recommendation.py
AIJobAssistant
Version : v1.3.1
"""

from models.job import Job


class Recommendation:

    @classmethod
    def evaluate(cls, job: Job) -> Job:

        score = job.total_score

        # Recommendation

        if score >= 90:

            job.decision = "APPLY"
            job.confidence = "Very High"
            job.recommendation = "★★★★★ Strong Apply"
            job.next_action = "Apply Immediately"

        elif score >= 75:

            job.decision = "APPLY"
            job.confidence = "High"
            job.recommendation = "★★★★☆ Apply"
            job.next_action = "Apply Today"

        elif score >= 60:

            job.decision = "REVIEW"
            job.confidence = "Medium"
            job.recommendation = "★★★☆☆ Manual Review"
            job.next_action = "Review Carefully"

        else:

            job.decision = "SKIP"
            job.confidence = "Low"
            job.recommendation = "★☆☆☆☆ Skip"
            job.next_action = "Skip"

        # Strength

        strengths = []

        if job.career_score:
            strengths.append("Job Performance Fit")

        if job.role_score >= 15:
            strengths.append("Hiring Probability")

        if job.leadership_score:
            strengths.append("Leadership")

        if job.security_score:
            strengths.append("Security")

        if job.salary_score:
            strengths.append("Salary")

        if job.language_score:
            strengths.append("Language")

        job.strength = ", ".join(strengths)

        # Weakness

        weaknesses = []

        if not job.career_score:
            weaknesses.append("Performance Fit")

        if job.role_score < 15:
            weaknesses.append("Hiring Probability")

        if not job.salary_score:
            weaknesses.append("Salary")

        if not job.language_score:
            weaknesses.append("Language")

        job.weak = ", ".join(weaknesses)

        # Reason

        if job.decision == "APPLY":

            job.reason = (
                "High hiring probability with strong job performance fit."
            )

        elif job.decision == "REVIEW":

            job.reason = (
                "Potential opportunity. Manual review recommended."
            )

        else:

            job.reason = (
                "Low hiring probability or insufficient job fit."
            )

        return job