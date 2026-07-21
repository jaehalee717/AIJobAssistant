"""
CV Service
AIJobAssistant
Version : v2.0.0
"""

from modules.apply.clipboard_service import ClipboardService


class CVService:

    def __init__(
        self,
        ai,
        prompt_builder,
        cv_generator,
    ):

        self.ai = ai
        self.prompt_builder = prompt_builder
        self.cv_generator = cv_generator

        self.clipboard = ClipboardService()

    def run(
        self,
        job,
        output,
    ) -> None:

        prompt = self.prompt_builder.build_cv_prompt(
            job,
        )

        self.ai.generate_cv(
            prompt,
        )

        cv_text = self.clipboard.wait_changed(
            prompt,
        )

        self.cv_generator.generate(
            output=output,
            profile=cv_text,
            competencies="",
            tai="",
            brazil="",
            spain="",
        )