"""
CL Service
AIJobAssistant
Version : v2.0.0
"""

from modules.apply.clipboard_service import ClipboardService


class CLService:

    def __init__(
        self,
        ai,
        prompt_builder,
        cl_generator,
    ):

        self.ai = ai
        self.prompt_builder = prompt_builder
        self.cl_generator = cl_generator

        self.clipboard = ClipboardService()

    def run(
        self,
        job,
        output,
    ) -> None:

        prompt = self.prompt_builder.build_cl_prompt(
            job,
        )

        self.ai.generate_cl(
            prompt,
        )

        cl_text = self.clipboard.wait_changed(
            prompt,
        )

        self.cl_generator.generate(
            output=output,
            letter=cl_text,
        )