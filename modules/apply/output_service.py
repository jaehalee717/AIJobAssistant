"""
Output Service
AIJobAssistant
Version : v1.5.2
"""

from modules.pdf_converter import PDFConverter
from modules.repository.job_repository import JobRepository


class OutputService:

    @staticmethod
    def run(
        job,
        output,
    ):

        pdf = PDFConverter()

        pdf.convert(
            output.get_cv_docx_path(),
            output.get_cv_pdf_path(),
        )

        pdf.convert(
            output.get_cl_docx_path(),
            output.get_cl_pdf_path(),
        )

        pdf.close()

        output.save_job_description(
            job.raw_html,
        )

        output.save_salary(
            job.salary,
        )

        output.save_report(
            job,
        )

        if job.apply_url:

            JobRepository().update_applied(
                job.apply_url,
            )