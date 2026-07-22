import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT),
)

from pathlib import Path

from modules.report.report_writer import ReportWriter


class DummyJob:

    def __init__(
        self,
        company,
        position,
    ):
        self.company = company
        self.position = position
        self.location = "Spain"
        self.score = 95
        self.recommendation = "APPLY"


def test_report_writer():

    jobs = [
        DummyJob(
            "Google",
            "IT Manager",
        ),
        DummyJob(
            "Amazon",
            "Security Manager",
        ),
    ]

    output = Path(
        "output/test_report.docx"
    )

    ReportWriter.write(
        jobs,
        output,
    )

    assert output.exists()