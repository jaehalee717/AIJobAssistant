"""
modules/apply_service.py
AIJobAssistant
Version : v2.1.0
"""

from config import (
    CL_TEMPLATE,
    CV_TEMPLATE,
    PROJECT_ROOT,
)

from modules.ai_generator import AIGenerator
from modules.apply.cl_service import CLService
from modules.apply.cv_service import CVService
from modules.apply.output_service import OutputService
from modules.apply_workflow import ApplyWorkflow
from modules.cl_generator import CLGenerator
from modules.cv_generator import CVGenerator
from modules.knowledge_loader import KnowledgeLoader
from modules.prompt_builder import PromptBuilder
from modules.repository.job_repository import JobRepository


class ApplyService:

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

        ai = AIGenerator()

        repository = JobRepository()

        cv_service = CVService(
            ai=ai,
            prompt_builder=prompt_builder,
            cv_generator=CVGenerator(
                CV_TEMPLATE,
            ),
        )

        cl_service = CLService(
            ai=ai,
            prompt_builder=prompt_builder,
            cl_generator=CLGenerator(
                CL_TEMPLATE,
            ),
        )

        self.workflow = ApplyWorkflow(
            repository=repository,
            cv_service=cv_service,
            cl_service=cl_service,
            output_service=OutputService,
        )

    def run(
        self,
    ) -> None:

        self.workflow.run()