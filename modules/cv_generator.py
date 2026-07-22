"""
modules/cv_generator.py

AIJobAssistant
Version : v6.0.0
"""

from pathlib import Path

from modules.ai_generator import AIGenerator
from modules.report.cv_quality_checker import CVQualityChecker
from modules.report.cv_writer import CVWriter
from modules.report.generation_service import GenerationService
from modules.report.response_validator import ResponseValidator
from modules.report.retry_prompt import RetryPrompt


class CVGenerator:

    MAX_RETRIES = 3

    def __init__(
        self,
        template,
        prompt_builder,
        ai_generator: AIGenerator,
    ):

        self.template = template
        self.prompt_builder = prompt_builder
        self.ai_generator = ai_generator

    def generate(
        self,
        job,
        output_file,
    ) -> None:

        prompt = self.prompt_builder.build_cv_prompt(
            job,
        )

        self._save_prompt(
            output_file,
            prompt,
        )

        output_dir = Path(
            output_file,
        ).parent

        last_error = None

        for attempt in range(
            1,
            self.MAX_RETRIES + 1,
        ):

            started = GenerationService.start()

            ai_text = self.ai_generator.generate_cv(
                prompt,
            )

            self._save_response(
                output_file,
                ai_text,
            )

            try:

                ResponseValidator.validate_cv(
                    ai_text,
                )

                CVQualityChecker.validate(
                    ai_text,
                )

                CVWriter.write(
                    template=self.template,
                    output=output_file,
                    ai_text=ai_text,
                )

                GenerationService.finish(
                    output_dir=output_dir,
                    document_type="CV",
                    attempt=attempt,
                    prompt=prompt,
                    response=ai_text,
                    start_time=started,
                    success=True,
                )

                return

            except Exception as e:

                last_error = e

                GenerationService.finish(
                    output_dir=output_dir,
                    document_type="CV",
                    attempt=attempt,
                    prompt=prompt,
                    response=ai_text,
                    start_time=started,
                    success=False,
                    error=str(
                        e,
                    ),
                )

                prompt = RetryPrompt.build(
                    prompt,
                    e,
                )

                self._save_prompt(
                    output_file,
                    prompt,
                )

        raise last_error

    @staticmethod
    def _save_prompt(
        output_file,
        prompt,
    ):

        (
            Path(
                output_file,
            ).parent
            / "CV_Prompt.txt"
        ).write_text(
            prompt,
            encoding="utf-8",
        )

    @staticmethod
    def _save_response(
        output_file,
        response,
    ):

        (
            Path(
                output_file,
            ).parent
            / "CV_Response.txt"
        ).write_text(
            response,
            encoding="utf-8",
        )