"""
reset_workflow.py

AIJobAssistant
Version : v2.0.0
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
        SET status = 'READY_TO_DETAIL',
            applied = 0
        WHERE status IN (
            'DETAIL_COMPLETED',
            'READY_TO_APPLY',
            'APPLIED'
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