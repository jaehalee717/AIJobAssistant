"""
modules/apply_service.py
AIJobAssistant
Version : v1.5.2
"""

from config import PROJECT_ROOT

from modules.apply.cv_service import CVService
from modules.apply.cl_service import CLService
from modules.apply.output_service import OutputService

from modules.ai_generator import AIGenerator
from modules.cl_generator import CLGenerator
from modules.cv_generator import CVGenerator
from modules.knowledge_loader import KnowledgeLoader
from modules.output_manager import OutputManager
from modules.prompt_builder import PromptBuilder


class ApplyService:

    def __init__(self):

        self.knowledge = KnowledgeLoader(
            PROJECT_ROOT / "knowledge"
        )

        self.knowledge.load()

        self.prompt_builder = PromptBuilder(
            self.knowledge
        )

        self.ai = AIGenerator()

        self.cv_generator = CVGenerator(
            PROJECT_ROOT / "templates" / "Jaeha_Lee_CV.docx"
        )

        self.cl_generator = CLGenerator(
            PROJECT_ROOT / "templates" / "Jaeha_Lee_CL.docx"
        )

        self.cv_service = CVService(
            self.ai,
            self.prompt_builder,
            self.cv_generator,
        )

        self.cl_service = CLService(
            self.ai,
            self.prompt_builder,
            self.cl_generator,
        )

    def run(
        self,
        job,
    ):

        print("=" * 80)
        print("AIJobAssistant v1.5.2")
        print("Apply")
        print("=" * 80)

        output = OutputManager(
            job,
        )

        self.cv_service.run(
            job,
            output,
        )
        self.cl_service.run(
            job,
            output,
        )

        OutputService.run(
            job,
            output,
        )

        print()
        print("=" * 80)
        print("Completed.")
        print(output.output_dir)
        print("=" * 80)