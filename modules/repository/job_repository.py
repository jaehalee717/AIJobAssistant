"""
modules/repository/job_repository.py

AIJobAssistant
Version : v2.0.0
"""

import sqlite3

from config import DB_FILE
from constants import status
from constants import decision
from models.job import Job


class JobRepository:

    def __init__(self):
        self.db = DB_FILE

    def _connect(self):
        return sqlite3.connect(self.db)

    def _row_to_job(self, row):
        if row is None:
            return None

        job = Job()

        job.id = row["id"]
        job.company = row["company"]
        job.position = row["position"]
        job.location = row["location"]
        job.description = row["description"]
        job.raw_html = row["raw_html"]
        job.country = row["country"]
        job.city = row["city"]
        job.salary = row["salary"]
        job.apply_url = row["url"]
        job.match = row["ai_score"]
        job.decision = row["ai_decision"]
        job.reason = row["reason"]

        return job

    def exists(self, apply_url):
        if not apply_url:
            return False

        with self._connect() as conn:
            cur = conn.execute(
                "SELECT 1 FROM jobs WHERE url=?",
                (apply_url,),
            )
            return cur.fetchone() is not None

    def insert(self, job):
        with self._connect() as conn:
            cursor = conn.execute(
                """
                INSERT OR IGNORE INTO jobs
                (
                    company, position, location, description,
                    raw_html, country, city, url,
                    ai_score, ai_decision, status,
                    salary, date
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    job.company,
                    job.position,
                    job.location,
                    job.description,
                    job.raw_html,
                    job.country,
                    job.city,
                    job.apply_url,
                    job.match,
                    job.decision,
                    status.NEW,
                    job.salary,
                    job.date,
                ),
            )

            job.id = cursor.lastrowid
            conn.commit()

    def update(self, job):

        status_map = {
            decision.APPLY: status.READY_TO_DETAIL,
            decision.REVIEW: status.READY_TO_DETAIL,
            decision.SKIP: status.SKIPPED,
            decision.REJECT: status.REJECTED,
        }

        with self._connect() as conn:
            conn.execute(
                """
                UPDATE jobs
                SET ai_score=?, ai_decision=?, reason=?, status=?
                WHERE url=?
                """,
                (
                    job.match,
                    job.decision,
                    job.reason,
                    status_map.get(
                        job.decision,
                        status.READY_TO_DETAIL,
                    ),
                    job.apply_url,
                ),
            )

            conn.commit()

    def get_job_by_id(self, job_id):
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT * FROM jobs WHERE id=?",
                (job_id,),
            ).fetchone()

        return self._row_to_job(row)

    def get_ready_to_apply_job(self):
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                """
                SELECT *
                FROM jobs
                WHERE status=?
                ORDER BY id
                LIMIT 1
                """,
                (status.READY_TO_APPLY,),
            ).fetchone()

        return self._row_to_job(row)

    def get_new_jobs(self):
        return self.get_jobs_by_status(status.NEW)

    def get_jobs_by_status(self, value):
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(
                """
                SELECT *
                FROM jobs
                WHERE status=?
                ORDER BY id
                """,
                (value,),
            ).fetchall()

        return [
            self._row_to_job(row)
            for row in rows
        ]

    def get_jobs_by_ids(self, job_ids):
        return [
            job
            for job in (
                self.get_job_by_id(job_id)
                for job_id in job_ids
            )
            if job is not None
        ]

    def update_status(self, apply_url, value):
        with self._connect() as conn:
            conn.execute(
                """
                UPDATE jobs
                SET status=?
                WHERE url=?
                """,
                (value, apply_url),
            )
            conn.commit()

    def update_applied(self, apply_url):
        with self._connect() as conn:
            conn.execute(
                """
                UPDATE jobs
                SET status=?, applied=1
                WHERE url=?
                """,
                (status.APPLIED, apply_url),
            )
            conn.commit()

    def mark_ready_to_detail(self, job_id):
        self._update_status_by_id(
            job_id,
            status.READY_TO_DETAIL,
        )

    def mark_detail_completed(self, job_id):
        self._update_status_by_id(
            job_id,
            status.DETAIL_COMPLETED,
        )

    def _update_status_by_id(self, job_id, value):
        with self._connect() as conn:
            conn.execute(
                """
                UPDATE jobs
                SET status=?
                WHERE id=?
                """,
                (value, job_id),
            )
            conn.commit()

    def update_detail_result(self, job):
        with self._connect() as conn:
            conn.execute(
                """
                UPDATE jobs
                SET ai_score=?, ai_decision=?, salary=?,
                    reason=?, status=?
                WHERE id=?
                """,
                (
                    job.match,
                    job.decision,
                    job.salary,
                    job.reason,
                    status.READY_TO_APPLY,
                    job.id,
                ),
            )
            conn.commit()
