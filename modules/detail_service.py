"""
modules/detail_service.py

AIJobAssistant
Version : v3.0.0
"""

from config import PROJECT_ROOT

from modules.ai_generator import AIGenerator
from modules.detail_parser import DetailParser
from modules.knowledge_loader import KnowledgeLoader
from modules.prompt.prompt_builder import PromptBuilder
from modules.repository.job_repository import JobRepository
from modules.workflow.detail_workflow import DetailWorkflow


class DetailService:

    def __init__(
        self,
    ):

        knowledge = KnowledgeLoader(
            PROJECT_ROOT / "knowledge",
        )

        knowledge.load()

        prompt_builder = PromptBuilder(
            knowledge,
        )

        repository = JobRepository()

        ai = AIGenerator()

        parser = DetailParser()

        self.workflow = DetailWorkflow(
            repository=repository,
            prompt_builder=prompt_builder,
            ai_generator=ai,
            parser=parser,
        )

    def run(
        self,
    ) -> None:

        self.workflow.run()