"""
job_repository.py
AIJobAssistant
Version : v1.5.0
"""

import sqlite3

from config import DB_FILE
from models.job import Job


class JobRepository:

    def __init__(self):

        self.db = DB_FILE


    def exists(
        self,
        apply_url: str,
    ) -> bool:

        if not apply_url:
            return False

        with sqlite3.connect(self.db) as conn:

            cur = conn.cursor()

            cur.execute(
                "SELECT 1 FROM jobs WHERE url=?",
                (apply_url,),
            )

            return cur.fetchone() is not None


    def insert(
        self,
        job: Job,
    ):

        with sqlite3.connect(self.db) as conn:

            conn.execute(
                """
                INSERT OR IGNORE INTO jobs
                (
                    company,
                    position,

                    location,
                    description,

                    country,
                    city,

                    url,

                    ai_score,
                    ai_decision,

                    status,

                    salary,

                    date
                )
                VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    job.company,
                    job.position,

                    job.location,
                    job.description,

                    job.country,
                    job.city,

                    job.apply_url,

                    job.match,
                    job.decision,

                    "NEW",

                    job.salary,

                    job.date,
                ),
            )

            conn.commit()


    def update(
        self,
        job: Job,
    ):

        status_map = {
            "APPLY": "READY_TO_APPLY",
            "REVIEW": "READY_TO_APPLY",
            "SKIP": "SKIPPED",
            "REJECT": "REJECTED",
        }

        status = status_map.get(
            job.decision,
            "REVIEW",
        )


        with sqlite3.connect(self.db) as conn:

            conn.execute(
                """
                UPDATE jobs
                SET
                    ai_score=?,
                    ai_decision=?,
                    reason=?,
                    status=?
                WHERE url=?
                """,
                (
                    job.match,
                    job.decision,
                    job.reason,
                    status,
                    job.apply_url,
                ),
            )

            conn.commit()


    def get_ready_to_apply_job(
        self,
    ) -> Job | None:

        with sqlite3.connect(self.db) as conn:

            conn.row_factory = sqlite3.Row

            cur = conn.cursor()

            cur.execute(
                """
                SELECT *
                FROM jobs
                WHERE status='READY_TO_APPLY'
                ORDER BY id
                LIMIT 1
                """
            )

            row = cur.fetchone()


            if row is None:

                return None


            job = Job()

            job.company = row["company"]

            job.position = row["position"]


            job.location = row["location"]

            job.description = row["description"]


            job.country = row["country"]

            job.city = row["city"]


            job.salary = row["salary"]

            job.apply_url = row["url"]

            job.reason = row["reason"]


            return job


    def update_applied(
        self,
        apply_url: str,
    ):

        with sqlite3.connect(self.db) as conn:

            conn.execute(
                """
                UPDATE jobs
                SET
                    status='APPLIED',
                    applied=1
                WHERE url=?
                """,
                (apply_url,),
            )

            conn.commit()


    def update_status(
        self,
        apply_url: str,
        status: str,
    ):

        with sqlite3.connect(self.db) as conn:

            conn.execute(
                """
                UPDATE jobs
                SET status=?
                WHERE url=?
                """,
                (
                    status,
                    apply_url,
                ),
            )

            conn.commit()