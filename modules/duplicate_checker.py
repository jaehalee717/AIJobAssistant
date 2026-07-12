"""
duplicate_checker.py
v0.8

SQLite Duplicate Checker

Rule
- URL exists -> Duplicate
- URL not exists -> New
"""

import sqlite3
from pathlib import Path


class DuplicateChecker:

    def __init__(self, db_path: str):
        self.db_path = Path(db_path)

    def is_duplicate(self, url: str) -> bool:

        if not url:
            return False

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM jobs
            WHERE url = ?
            LIMIT 1
            """,
            (url,),
        )

        result = cursor.fetchone()

        conn.close()

        return result is not None

    def save(self, url: str):

        if not url:
            return

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT OR IGNORE INTO jobs(url)
            VALUES(?)
            """,
            (url,),
        )

        conn.commit()
        conn.close()