"""
modules/apply_workflow.py
AIJobAssistant
Version : v2.1.0
"""

from modules.console import console
from modules.output_manager import OutputManager


class ApplyWorkflow:

    def __init__(
        self,
        repository,
        cv_service,
        cl_service,
        output_service,
    ):

        self.repository = repository
        self.cv_service = cv_service
        self.cl_service = cl_service
        self.output_service = output_service

    def run(
        self,
    ) -> None:

        jobs = self.repository.get_jobs_by_status(
            "READY_TO_APPLY",
        )

        if not jobs:

            console.warning(
                "No READY_TO_APPLY jobs."
            )

            return

        console.clear()

        console.header(
            step="3/3",
            title="Apply",
            current=1,
            total=3,
        )

        for job in jobs:

            console.job(
                job,
            )

        print()

        job_ids = [
            int(x.strip())
            for x in input(
                "Job No : "
            ).split(",")
            if x.strip()
        ]

        selected_jobs = self.repository.get_jobs_by_ids(
            job_ids,
        )

        total = len(
            selected_jobs,
        )

        for current, job in enumerate(
            selected_jobs,
            start=1,
        ):

            console.clear()

            console.header(
                step="3/3",
                title="Apply",
                current=current,
                total=total,
            )

            console.job(
                job,
            )

            output = OutputManager(
                job,
            )

            self.cv_service.run(
                job,
                output,
            )

            self.cl_service.run(
                job,
                output,
            )

            self.output_service.run(
                job,
                output,
            )

            self.repository.update_applied(
                job.apply_url,
            )

        console.success(
            "Apply completed."
        )