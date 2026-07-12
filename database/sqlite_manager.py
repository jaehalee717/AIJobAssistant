"""
SQLite Manager
AIJobAssistant v0.8
"""

import sqlite3

from config import DB_FILE


class SQLiteManager:

    def __init__(self):

        self.conn = sqlite3.connect(DB_FILE)

        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()

    def close(self):

        self.conn.close()

    def is_duplicate(self, url):

        self.cursor.execute(
            """
            SELECT id
            FROM jobs
            WHERE url=?
            """,
            (url,),
        )

        return self.cursor.fetchone() is not None

    def insert_job(self, job):

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
        url,
        status,
    ):

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