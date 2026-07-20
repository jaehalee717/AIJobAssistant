"""
modules/workflow/analysis_workflow.py

AIJobAssistant
Version : v2.1.0
"""

from pathlib import Path

from models.job import Job
from modules.analysis.service import AnalysisService
from modules.report.report_service import ReportService


class AnalysisWorkflow:

    def __init__(
        self,
        repository,
        analysis_service: AnalysisService,
    ):
        self.repository = repository
        self.analysis_service = analysis_service

    def get_next_job(
        self,
    ) -> Job | None:

        jobs = self.repository.get_new_jobs()

        if not jobs:
            return None

        return jobs[0]

    def create_prompt(
        self,
        job: Job,
    ) -> str:

        return self.analysis_service.create_prompt(
            job,
        )

    def import_result(
        self,
        job: Job,
        ai_result: str,
    ) -> Job:

        return self.analysis_service.analyze(
            job,
            ai_result,
        )

    def create_report(
        self,
        output_dir: Path,
    ):

        jobs = self.repository.get_jobs_by_status(
            "READY_TO_APPLY",
        )

        return ReportService.create(
            jobs=jobs,
            output_dir=output_dir,
            filename="Analysis_Report.docx",
        )