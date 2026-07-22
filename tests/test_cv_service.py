"""
tests/test_cv_service.py
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

from models.job import Job
from modules.apply.cv_service import CVService
from modules.output_manager import OutputManager

class DummyAI:

    def generate_cv(
        self,
        prompt,
    ):
        self.prompt = prompt


class DummyPromptBuilder:

    def build_cv_prompt(
        self,
        job,
    ):
        return "CV PROMPT"


class DummyCVGenerator:

    def __init__(self):
        self.called = False

    def generate(
        self,
        output,
        profile,
        competencies,
        tai,
        brazil,
        spain,
    ):
        self.called = True

        path = output.get_cv_docx_path()

        path.write_text(
            profile,
            encoding="utf-8",
        )

        return path


class DummyClipboard:

    def wait_changed(
        self,
        expected,
    ):
        return "Generated CV"


def create_job():

    job = Job()

    job.company = "Microsoft"
    job.position = "IT Manager"
    job.country = "Spain"

    return job


def test_cv_service():

    generator = DummyCVGenerator()

    service = CVService(
        DummyAI(),
        DummyPromptBuilder(),
        generator,
    )

    service.clipboard = DummyClipboard()

    output = OutputManager(
        create_job(),
    )

    service.run(
        create_job(),
        output,
    )

    assert generator.called

    assert output.get_cv_docx_path().exists()

    assert (
        output.get_cv_docx_path().read_text(
            encoding="utf-8",
        )
        == "Generated CV"
    )