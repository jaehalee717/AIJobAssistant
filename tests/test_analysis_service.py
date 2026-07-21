"""
tests/test_analysis_service.py
AIJobAssistant
Version : v2.0.0
"""

from models.job import Job
from modules.analysis.service import AnalysisService


class DummyPromptBuilder:

    def build_analysis_prompt(
        self,
        job,
    ):
        return "PROMPT"


class DummyAI:

    def generate_analysis(
        self,
        prompt,
    ):
        self.prompt = prompt


class DummyRepository:

    def __init__(self):
        self.updated = False

    def update(
        self,
        job,
    ):
        self.updated = True


def test_create_prompt():

    service = AnalysisService(
        DummyPromptBuilder(),
        DummyAI(),
        DummyRepository(),
    )

    prompt = service.create_prompt(
        Job(),
    )

    assert prompt == "PROMPT"