"""
tests/test_output_service.py
AIJobAssistant
Version : v2.0.0
"""

from models.job import Job
from modules.apply.output_service import OutputService
from modules.output_manager import OutputManager


class DummyPDFConverter:

    def convert(
        self,
        src,
        dst,
    ):
        dst.write_text(
            "PDF",
            encoding="utf-8",
        )

    def close(
        self,
    ):
        pass


def create_job() -> Job:

    job = Job()

    job.company = "Microsoft"
    job.position = "IT Manager"
    job.country = "Spain"

    job.location = "Madrid"
    job.salary = "€70,000"

    job.raw_html = "<html>TEST</html>"
    job.apply_url = ""

    job.match = 95
    job.confidence = 98
    job.strength = "Infrastructure"
    job.weak = "Azure"
    job.reason = "Good Fit"
    job.recommendation = "Apply"
    job.next_action = "Generate"

    return job


def test_output_service(
    monkeypatch,
):

    from modules.apply import output_service

    monkeypatch.setattr(
        output_service,
        "PDFConverter",
        DummyPDFConverter,
    )

    job = create_job()

    output = OutputManager(
        job,
    )

    output.get_cv_docx_path().write_text(
        "CV",
        encoding="utf-8",
    )

    output.get_cl_docx_path().write_text(
        "CL",
        encoding="utf-8",
    )

    OutputService.run(
        job,
        output,
    )

    assert output.get_cv_pdf_path().exists()

    assert output.get_cl_pdf_path().exists()

    assert output.get_jd_html_path().exists()

    assert output.get_analysis_path().exists()

    assert output.get_salary_path().exists()