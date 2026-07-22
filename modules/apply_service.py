"""
modules/apply_service.py

AIJobAssistant
Version : v5.0.0
"""

from config import (
    CL_TEMPLATE,
    CV_TEMPLATE,
    PROJECT_ROOT,
)

from modules.ai_generator import AIGenerator
from modules.cl_generator import CLGenerator
from modules.cv_generator import CVGenerator
from modules.knowledge_loader import KnowledgeLoader
from modules.pdf_converter import PDFConverter
from modules.prompt.prompt_builder import PromptBuilder
from modules.repository.job_repository import JobRepository
from modules.workflow.apply_workflow import ApplyWorkflow


class ApplyService:

    def __init__(
        self,
    ):

        knowledge_loader = KnowledgeLoader(
            PROJECT_ROOT / "knowledge",
        )

        knowledge_loader.load()

        prompt_builder = PromptBuilder(
            knowledge_loader,
        )

        ai_generator = AIGenerator()

        repository = JobRepository()

        cv_generator = CVGenerator(
            template=CV_TEMPLATE,
            prompt_builder=prompt_builder,
            ai_generator=ai_generator,
        )

        cl_generator = CLGenerator(
            template=CL_TEMPLATE,
            prompt_builder=prompt_builder,
            ai_generator=ai_generator,
        )

        pdf_converter = PDFConverter()

        self.workflow = ApplyWorkflow(
            repository=repository,
            cv_generator=cv_generator,
            cl_generator=cl_generator,
            pdf_converter=pdf_converter,
        )

    def run(
        self,
    ) -> None:

        self.workflow.run()