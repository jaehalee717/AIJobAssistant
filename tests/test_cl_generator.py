"""
tests/test_cl_generator.py
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

from config import CL_TEMPLATE
from models.job import Job
from modules.cl_generator import CLGenerator
from modules.output_manager import OutputManager


def create_job() -> Job:

    job = Job()

    job.company = "Microsoft"
    job.position = "IT Manager"
    job.country = "Spain"

    return job


def test_generate_cl():

    output = OutputManager(
        create_job(),
    )

    generator = CLGenerator(
        CL_TEMPLATE,
    )

    path = generator.generate(
        output=output,
        letter="Test Cover Letter",
    )

    assert path.exists()

    assert (
        path
        == output.get_cl_docx_path()
    )