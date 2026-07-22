"""
tests/test_cv_generator.py
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

from config import CV_TEMPLATE
from models.job import Job
from modules.cv_generator import CVGenerator
from modules.output_manager import OutputManager


def create_job() -> Job:

    job = Job()

    job.company = "Microsoft"
    job.position = "IT Manager"
    job.country = "Spain"

    return job


def test_generate_cv():

    output = OutputManager(
        create_job(),
    )

    generator = CVGenerator(
        CV_TEMPLATE,
    )

    path = generator.generate(
        output=output,
        profile="Profile",
        competencies="Competencies",
        tai="TAI",
        brazil="Brazil",
        spain="Spain",
    )

    assert path.exists()
    assert path == output.get_cv_docx_path()