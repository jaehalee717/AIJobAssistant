"""
score_engine.py
AIJobAssistant
Version : v1.3.0
"""

from models.job import Job

from modules.score.hard_rule import HardRule
from modules.score.score_calculator import ScoreCalculator
from modules.score.recommendation import Recommendation


class ScoreEngine:

    @classmethod
    def evaluate(cls, job: Job) -> Job:

        passed, reason = HardRule.evaluate(job)

        if not passed:

            job.total_score = 0
            job.match = 0

            job.decision = "REJECT"
            job.confidence = "Very High"

            job.recommendation = "Do Not Apply"
            job.next_action = "Reject"

            job.reason = reason

            return job

        job = ScoreCalculator.calculate(job)

        job = Recommendation.evaluate(job)

        return job