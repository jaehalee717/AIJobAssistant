"""
reset_detail.py
AIJobAssistant
Version : v1.1.0
"""

import sqlite3

from config import DB_FILE


def main():

    conn = sqlite3.connect(
        DB_FILE,
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE jobs
        SET status = 'READY_TO_DETAIL'
        WHERE status IN (
            'DETAIL_COMPLETED',
            'READY_TO_APPLY'
        )
        """
    )

    count = cursor.rowcount

    conn.commit()

    conn.close()

    print(
        f"{count} job(s) restored to READY_TO_DETAIL."
    )


if __name__ == "__main__":
    main()