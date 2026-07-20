"""
application_workflow.py
AIJobAssistant
Version : v1.5.2
"""

from modules.apply_service import ApplyService
from modules.documents.report_generator import ReportGenerator
from modules.repository.job_repository import JobRepository
from modules.workflow.job_processor import JobProcessor


class ApplicationWorkflow:

    def __init__(self):

        self.repository = JobRepository()

        self.report = ReportGenerator(
            "reports",
        )

        self.apply_service = ApplyService()

        self.processed = 0
        self.skipped = 0
        self.failed = 0

    def run(
        self,
        jobs,
    ):

        for job in jobs:

            try:

                if (
                    job.apply_url
                    and self.repository.exists(
                        job.apply_url,
                    )
                ):
                    self.skipped += 1
                    continue

                self.repository.insert(
                    job,
                )

                job, result = JobProcessor.process(
                    job,
                    self.repository,
                )

                if job is None:
                    self.skipped += 1
                    continue

                self.repository.update(
                    job,
                )

                self.report.generate(
                    job,
                )

                if job.decision in (
                    "APPLY",
                    "REVIEW",
                ):
                    self.apply_service.run(
                        job,
                    )

                self.processed += 1

            except Exception as e:

                print(e)

                self.failed += 1

        return self.report.save(
            processed=self.processed,
            skipped=self.skipped,
            failed=self.failed,
        )