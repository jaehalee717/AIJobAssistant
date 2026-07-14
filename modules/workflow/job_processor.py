"""
job_processor.py
AIJobAssistant
Version : v1.5.0
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

        job = JDParser.parse(job)

        job = ScoreEngine.evaluate(job)

        return job, "processed"