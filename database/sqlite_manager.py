"""
SQLite Manager
AIJobAssistant v1.5.0
"""

from __future__ import annotations

import sqlite3

from config import DB_FILE


class SQLiteManager:

    def __init__(self):

        self.conn = sqlite3.connect(DB_FILE)

        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()

    def close(self):

        self.conn.close()

    def is_duplicate(
        self,
        url: str,
    ) -> bool:

        self.cursor.execute(
            """
            SELECT id
            FROM jobs
            WHERE url=?
            """,
            (url,),
        )

        return self.cursor.fetchone() is not None

    def insert_job(
        self,
        job: dict,
    ) -> None:

        self.cursor.execute(
            """
            INSERT INTO jobs
            (
                company,
                position,
                country,
                city,
                url,
                ai_score,
                ai_decision,
                user_decision,
                status,
                applied,
                skip,
                interview1,
                interview2,
                interview3,
                offer,
                reject,
                salary,
                date,
                reason
            )
            VALUES
            (
                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?,?
            )
            """,
            (
                job.get("company"),
                job.get("position"),
                job.get("country"),
                job.get("city"),
                job.get("url"),
                job.get("ai_score"),
                job.get("ai_decision"),
                "",
                "NEW",
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                job.get("salary"),
                job.get("date"),
                job.get("reason"),
            ),
        )

        self.conn.commit()

    def update_status(
        self,
        url: str,
        status: str,
    ) -> None:

        self.cursor.execute(
            """
            UPDATE jobs
            SET status=?
            WHERE url=?
            """,
            (
                status,
                url,
            ),
        )

        self.conn.commit()

    def get_ready_to_apply_job(
        self,
    ) -> dict | None:

        self.cursor.execute(
            """
            SELECT *
            FROM jobs
            WHERE status = ?
            ORDER BY id
            LIMIT 1
            """,
            ("READY_TO_APPLY",),
        )

        row = self.cursor.fetchone()

        if row is None:
            return None

        return dict(row)

    def update_apply_status(
        self,
        url: str,
    ) -> None:

        self.cursor.execute(
            """
            UPDATE jobs
            SET
                status = 'APPLIED',
                applied = 1
            WHERE url = ?
            """,
            (url,),
        )

        self.conn.commit()