"""
database.py
AIJobAssistant v1.5.0

SQLite Database Manager
"""

import sqlite3
from pathlib import Path


class Database:

    def __init__(
        self,
        db_path: str,
    ):

        self.db_path = Path(db_path)


    def initialize(self):

        self.db_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS jobs (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                company TEXT,
                position TEXT,

                location TEXT,
                description TEXT,

                raw_html TEXT,

                country TEXT,
                city TEXT,

                url TEXT UNIQUE,

                ai_score INTEGER,
                ai_decision TEXT,
                user_decision TEXT,

                status TEXT,

                applied INTEGER DEFAULT 0,
                skipped INTEGER DEFAULT 0,

                interview1 INTEGER DEFAULT 0,
                interview2 INTEGER DEFAULT 0,
                interview3 INTEGER DEFAULT 0,

                offer INTEGER DEFAULT 0,
                reject_flag INTEGER DEFAULT 0,

                salary TEXT,

                date TEXT,

                reason TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.commit()

        conn.close()


    def connect(self):

        return sqlite3.connect(
            self.db_path
        )