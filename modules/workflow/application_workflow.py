"""
application_workflow.py
AIJobAssistant
Version : v2.0.0
"""
import traceback

from modules.documents.report_generator import ReportGenerator
from modules.repository.job_repository import JobRepository
from modules.workflow.job_processor import JobProcessor


class ApplicationWorkflow:

    def __init__(
        self,
    ):

        self.repository = JobRepository()

        self.report = ReportGenerator(
            "reports",
        )

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

                job, _ = JobProcessor.process(
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

                    self.repository.mark_ready_to_detail(
                        job.id,
                    )

                else:

                    self.repository.update_status(
                        job.apply_url,
                        "SKIPPED",
                    )

                self.processed += 1

            except Exception:

                traceback.print_exc()

                self.failed += 1

        return self.report.save(
            processed=self.processed,
            skipped=self.skipped,
            failed=self.failed,
        )