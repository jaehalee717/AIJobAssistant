"""
tests/test_output_manager.py
AIJobAssistant
Version : v2.0.0
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT),
)

from modules.output_manager import OutputManager
from models.job import Job


def create_job() -> Job:

    job = Job()

    job.company = "Microsoft"
    job.position = "IT Manager"
    job.country = "Spain"
    job.location = "Madrid"

    job.salary = "€70,000"
    job.match = 92
    job.confidence = 95

    job.strength = "Infrastructure"
    job.weak = "Azure"

    job.reason = "Strong overall fit."
    job.recommendation = "Apply"
    job.next_action = "Generate CV"

    job.apply_url = "https://example.com"

    return job


def test_output_directory():

    output = OutputManager(
        create_job(),
    )

    assert output.get_output_dir().exists()
    assert output.get_output_dir().is_dir()


def test_folder_name():

    output = OutputManager(
        create_job(),
    )

    assert output.get_folder_name().startswith(
        "Microsoft_IT_Manager_Spain_"
    )


def test_paths():

    output = OutputManager(
        create_job(),
    )

    assert (
        output.get_jd_html_path().name
        == f"{output.get_folder_name()}.html"
    )

    assert (
        output.get_analysis_path().name
        == "Analysis.md"
    )

    assert (
        output.get_salary_path().name
        == "Salary.txt"
    )

    assert (
        output.get_cv_docx_path().name
        == "Jaeha_Lee_CV.docx"
    )

    assert (
        output.get_cv_pdf_path().name
        == "Jaeha_Lee_CV.pdf"
    )

    assert (
        output.get_cl_docx_path().name
        == "Jaeha_Lee_CL.docx"
    )

    assert (
        output.get_cl_pdf_path().name
        == "Jaeha_Lee_CL.pdf"
    )


def test_save_job_description():

    output = OutputManager(
        create_job(),
    )

    output.save_job_description(
        "<html>TEST</html>",
    )

    path = output.get_jd_html_path()

    assert path.exists()

    assert (
        path.read_text(
            encoding="utf-8",
        )
        == "<html>TEST</html>"
    )


def test_save_salary():

    output = OutputManager(
        create_job(),
    )

    output.save_salary(
        "€70,000",
    )

    path = output.get_salary_path()

    assert path.exists()

    assert (
        path.read_text(
            encoding="utf-8",
        )
        == "€70,000"
    )


def test_save_analysis():

    output = OutputManager(
        create_job(),
    )

    output.save_analysis()

    path = output.get_analysis_path()

    assert path.exists()

    text = path.read_text(
        encoding="utf-8",
    )

    assert "Microsoft" in text
    assert "IT Manager" in text
    assert "Apply" in text
    assert "https://example.com" in text