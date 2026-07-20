"""
CV Service
AIJobAssistant
Version : v1.5.4
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
    ):

        print("CV STEP 1")

        prompt = self.prompt_builder.build_cv_prompt(
            job,
        )

        print("CV STEP 2")

        self.ai.generate_cv(
            prompt,
        )

        print("CV STEP 3")

        print()
        print("=" * 80)
        print("Copy ChatGPT CV response (Ctrl+A, Ctrl+C)...")
        print("Waiting automatically...")
        print("=" * 80)

        cv_text = self.clipboard.wait_changed(
            prompt,
        )

        print("CV STEP 4")
        print(
            f"CV length: {len(cv_text)}"
        )

        self.cv_generator.generate(
            output_path=output.get_cv_docx_path(),
            profile=cv_text,
            competencies="",
            tai="",
            brazil="",
            spain="",
        )

        print("CV STEP 5")