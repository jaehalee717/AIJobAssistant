"""
modules/workflow/apply_workflow.py

AIJobAssistant
Version : v3.1.0
"""

from modules.console import console


class ApplyWorkflow:

    def __init__(
        self,
        repository,
        cv_generator,
        cl_generator,
        pdf_converter,
        output_service,
    ):

        self.repository = repository
        self.cv_generator = cv_generator
        self.cl_generator = cl_generator
        self.pdf_converter = pdf_converter
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
            total=len(jobs),
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

            files = self.output_service.create(
                job,
            )

            self.cv_generator.run(
                job,
                self.output_service.cv(
                    files,
                ),
            )

            self.cl_generator.run(
                job,
                self.output_service.cl(
                    files,
                ),
            )

            self.pdf_converter.convert(
                self.output_service.cv(
                    files,
                ),
            )

            self.pdf_converter.convert(
                self.output_service.cl(
                    files,
                ),
            )

            self.repository.update_applied(
                job.apply_url,
            )

        console.success(
            "Apply completed."
        )