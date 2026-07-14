"""
duplicate_checker.py
AIJobAssistant
Version : v1.2.3
"""

from models.job import Job


class DuplicateChecker:

    @staticmethod
    def is_duplicate(job: Job, jobs: list[Job]) -> bool:

        for item in jobs:

            if DuplicateChecker._same_job(job, item):
                return True

        return False

    @staticmethod
    def _same_job(job1: Job, job2: Job) -> bool:

        if job1.apply_url and job2.apply_url:
            if job1.apply_url == job2.apply_url:
                return True

        if (
            job1.company.strip().lower()
            == job2.company.strip().lower()
            and
            job1.position.strip().lower()
            == job2.position.strip().lower()
            and
            job1.location.strip().lower()
            == job2.location.strip().lower()
        ):
            return True

        return False