"""
tests/test_cl_service.py
AIJobAssistant
Version : v2.0.0
"""

from models.job import Job
from modules.apply.cl_service import CLService
from modules.output_manager import OutputManager


class DummyAI:

    def generate_cl(
        self,
        prompt,
    ):
        self.prompt = prompt


class DummyPromptBuilder:

    def build_cl_prompt(
        self,
        job,
    ):
        return "CL PROMPT"


class DummyCLGenerator:

    def __init__(self):
        self.called = False

    def generate(
        self,
        output,
        letter,
    ):
        self.called = True

        path = output.get_cl_docx_path()

        path.write_text(
            letter,
            encoding="utf-8",
        )

        return path


class DummyClipboard:

    def wait_changed(
        self,
        expected,
    ):
        return "Generated Cover Letter"


def create_job():

    job = Job()

    job.company = "Microsoft"
    job.position = "IT Manager"
    job.country = "Spain"

    return job


def test_cl_service():

    generator = DummyCLGenerator()

    service = CLService(
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

    assert output.get_cl_docx_path().exists()

    assert (
        output.get_cl_docx_path().read_text(
            encoding="utf-8",
        )
        == "Generated Cover Letter"
    )