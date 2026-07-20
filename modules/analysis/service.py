"""
modules/analysis/service.py

AIJobAssistant
Version : v2.0.0
"""

from __future__ import annotations

from models.job import Job

from modules.ai_generator import AIGenerator
from modules.analysis.result import AnalysisResultParser
from modules.prompt_builder import PromptBuilder
from modules.repository.job_repository import JobRepository


class AnalysisService:
    """ChatGPT 기반 1차 분석"""

    def __init__(
        self,
        prompt_builder: PromptBuilder,
        ai_generator: AIGenerator,
        repository: JobRepository,
    ):
        self.prompt_builder = prompt_builder
        self.ai_generator = ai_generator
        self.repository = repository

    def analyze(
        self,
        job: Job,
        ai_result: str,
    ) -> Job:
        """
        Parse ChatGPT result and update DB.
        """

        job = AnalysisResultParser.parse(
            ai_result,
            job,
        )

        self.repository.update(
            job,
        )

        return job

    def create_prompt(
        self,
        job: Job,
    ) -> str:

        prompt = self.prompt_builder.build_analysis_prompt(
            job,
        )

        self.ai_generator.generate_analysis(
            prompt,
        )

        return prompt