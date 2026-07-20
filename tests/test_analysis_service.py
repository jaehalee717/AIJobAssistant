from modules.analysis.service import AnalysisService
from models.job import Job


def test_analysis():

    job = Job()

    job.match = 90

    service = AnalysisService()

    result = service.analyze(
        [job]
    )

    assert result[0].decision == "APPLY"