"""
modules/prompt/prompt_builder.py

AIJobAssistant
Version : v1.0.0
"""

from .analysis_prompt import AnalysisPrompt
from .cl_prompt import CLPrompt
from .cv_prompt import CVPrompt
from .detail_analysis_prompt import DetailAnalysisPrompt


class PromptBuilder:

    def __init__(
        self,
        knowledge,
    ):

        self.knowledge = knowledge

    def build_cv_prompt(
        self,
        job,
    ) -> str:

        return CVPrompt.build(
            job,
            self.knowledge,
        )

    def build_cl_prompt(
        self,
        job,
    ) -> str:

        return CLPrompt.build(
            job,
            self.knowledge,
        )

    def build_analysis_prompt(
        self,
        job,
    ) -> str:

        return AnalysisPrompt.build(
            job,
            self.knowledge,
        )

    def build_detail_analysis_prompt(
        self,
        job,
    ) -> str:

        return DetailAnalysisPrompt.build(
            job,
            self.knowledge,
        )