"""
Repository Test
AIJobAssistant
"""

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(
    0,
    str(ROOT),
)

from config import DB_FILE
from constants import status
from models.job import Job
from modules.repository.job_repository import JobRepository


def main():

    # 테스트 데이터 삭제
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            "DELETE FROM jobs WHERE url=?",
            ("https://example.com/test",),
        )
        conn.commit()

    repo = JobRepository()

    job = Job()

    job.company = "Test Company"
    job.position = "IT Manager"

    job.location = "Madrid"
    job.country = "Spain"
    job.city = "Madrid"

    job.description = "Test Description"

    job.raw_html = """
<html>
<body>
<h1>Repository Test</h1>
</body>
</html>
"""

    job.apply_url = "https://example.com/test"

    job.match = 90
    job.decision = "REVIEW"

    job.salary = "70000"
    job.date = "2026-07-20"

    repo.insert(
        job,
    )

    repo.update(
        job,
    )

    loaded = repo.get_job_by_id(
        job.id,
    )

    assert loaded is not None
    assert loaded.company == job.company
    assert loaded.position == job.position
    assert loaded.raw_html == job.raw_html

    print("PASS")
    print(loaded.company)
    print(loaded.position)


if __name__ == "__main__":
    main()