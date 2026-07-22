"""
modules/workflow/detail_workflow.py
AIJobAssistant
Version : v2.2.2
"""

from datetime import datetime

from config import REPORT_DIR

from modules.console import console
from modules.report.detail_report_writer import DetailReportWriter


class DetailWorkflow:

    def __init__(
        self,
        repository,
        prompt_builder,
        ai_generator,
        parser,
    ):

        self.repository = repository
        self.prompt_builder = prompt_builder
        self.ai_generator = ai_generator
        self.parser = parser

    def run(
        self,
    ) -> None:

        jobs = self.repository.get_jobs_by_status(
            "READY_TO_DETAIL",
        )

        if not jobs:

            console.warning(
                "No READY_TO_DETAIL jobs."
            )

            return

        console.clear()

        console.header(
            step="2/3",
            title="Detail Analysis",
            current=1,
            total=3,
        )

        for job in jobs:

            print(
                f"{job.id:4d} | "
                f"{job.company} | "
                f"{job.position} | "
                f"{job.location}"
            )

        print()
        print("=" * 80)

        import sys

        sys.stdout.write(
            "Job No : "
        )

        sys.stdout.flush()

        job_no = sys.stdin.readline().strip()

        job_ids = [
            int(x.strip())
            for x in job_no.split(",")
            if x.strip()
        ]

        selected_jobs = self.repository.get_jobs_by_ids(
            job_ids,
        )

        if not selected_jobs:

            console.warning(
                "No jobs selected."
            )

            return

        for current, job in enumerate(
            selected_jobs,
            start=1,
        ):

            console.clear()

            console.header(
                step="2/3",
                title="Detail Analysis",
                current=current,
                total=len(selected_jobs),
            )

            console.job(
                job,
            )

            prompt = self.prompt_builder.build_detail_analysis_prompt(
                job,
            )

            self.ai_generator.generate_detail_analysis(
                prompt,
            )

            response = self.ai_generator.read_response()

            detail = self.parser.parse(
                response,
            )

            job.detail_result = detail

            job.decision = detail.recommendation
            job.match = detail.ats_match
            job.salary = detail.expected_salary
            job.reason = detail.reason

            self.repository.update_detail_result(
                job,
            )

        report_file = (
            REPORT_DIR
            / f"Detail_AIJobAssistant_{datetime.now():%Y%m%d_%H%M}.docx"
        )

        DetailReportWriter.write(
            selected_jobs,
            report_file,
        )

        console.success(
            f"Detail Report : {report_file.name}"
        )