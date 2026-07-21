"""
job_processor.py
AIJobAssistant
Version : v2.0.0
"""

from models.job import Job

from modules.jd_parser import JDParser
from modules.score_engine import ScoreEngine


class JobProcessor:

    @classmethod
    def process(
        cls,
        job: Job,
        repository,
    ) -> tuple[Job | None, str]:

        job = JDParser.parse(
            job,
        )

        job = ScoreEngine.evaluate(
            job,
        )

        if job is None:
            return None, "SKIPPED"

        return (
            job,
            job.decision,
        )