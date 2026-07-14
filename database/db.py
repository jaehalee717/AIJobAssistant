import sqlite3

from config import DB_FILE


def initialize_database():

    conn = sqlite3.connect(DB_FILE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        company TEXT,
        position TEXT,

        location TEXT,
        description TEXT,

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

        reason TEXT
    )
    """)

    conn.commit()

    conn.close()