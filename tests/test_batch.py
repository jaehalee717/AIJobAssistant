import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT),
)

from modules.analysis.batch import AnalysisBatch
from models.job import Job


def test_batch():

    jobs = [
        Job(),
        Job(),
    ]

    results = [
        """
        {
            "score":90,
            "decision":"APPLY",
            "reason":"Excellent match."
        }
        """,
        """
        {
            "score":65,
            "decision":"REVIEW",
            "reason":"Needs review."
        }
        """,
    ]

    parsed = AnalysisBatch.parse_results(
        jobs,
        results,
    )

    assert parsed[0].match == 90
    assert parsed[0].decision == "APPLY"

    assert parsed[1].match == 65
    assert parsed[1].decision == "REVIEW"