"""
modules/workflow/apply_workflow.py

AIJobAssistant
Version : v4.1.0
"""

from constants.status import (
    SKIPPED,
)
from modules.output_manager import OutputManager


class ApplyWorkflow:

    def __init__(
        self,
        repository,
        cv_generator,
        cl_generator,
        pdf_converter,
    ):

        self.repository = repository
        self.cv_generator = cv_generator
        self.cl_generator = cl_generator
        self.pdf_converter = pdf_converter

    def run(
        self,
    ):

        job = self.repository.get_ready_to_apply_job()

        if job is None:

            print(
                "\nNo jobs ready to apply."
            )

            return

        print(
            f"\nCompany : {job.company}"
        )

        print(
            f"Position : {job.position}"
        )

        answer = input(
            "\nApply? (Y/N): "
        ).strip().upper()

        if answer != "Y":

            self.repository.update_status(
                job.apply_url,
                SKIPPED,
            )

            return

        files = OutputManager.create(
            job,
        )

        self.cv_generator.generate(
            job,
            files["cv_file"],
        )

        self.cl_generator.generate(
            job,
            files["cl_file"],
        )

        self.pdf_converter.convert(
            files["cv_file"],
        )

        self.pdf_converter.convert(
            files["cl_file"],
        )

        self.repository.update_applied(
            job.apply_url,
        )

        print("\nGenerated Files")
        print(
            f"Output Folder : {files['output_dir']}"
        )
        print(
            f"CV           : {files['cv_file'].name}"
        )
        print(
            f"CV PDF       : {files['cv_file'].with_suffix('.pdf').name}"
        )
        print(
            f"CL           : {files['cl_file'].name}"
        )
        print(
            f"CL PDF       : {files['cl_file'].with_suffix('.pdf').name}"
        )

        print(
            "\nApplication package created."
        )