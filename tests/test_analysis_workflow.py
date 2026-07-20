from pathlib import Path

from modules.workflow.analysis_workflow import AnalysisWorkflow


class DummyRepository:

    def get_new_jobs(self):
        return []

    def get_jobs_by_status(
        self,
        status,
    ):
        return []


class DummyAnalysisService:

    def create_prompt(
        self,
        job,
    ):
        return "prompt"

    def analyze(
        self,
        job,
        result,
    ):
        return job


def test_analysis_workflow():

    workflow = AnalysisWorkflow(
        DummyRepository(),
        DummyAnalysisService(),
    )

    assert workflow.get_next_job() is None

    workflow.create_report(
        Path("output")
    )