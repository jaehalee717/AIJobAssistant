"""
CL Service
AIJobAssistant
Version : v1.5.4
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
    ):

        print("CL STEP 1")

        prompt = self.prompt_builder.build_cl_prompt(
            job,
        )

        print("CL STEP 2")

        self.ai.generate_cl(
            prompt,
        )

        print("CL STEP 3")

        print()
        print("=" * 80)
        print("Copy ChatGPT Cover Letter response (Ctrl+A, Ctrl+C)...")
        print("Waiting automatically...")
        print("=" * 80)

        cl_text = self.clipboard.wait_changed(
            prompt,
        )

        print("CL STEP 4")
        print(
            f"CL length: {len(cl_text)}"
        )

        self.cl_generator.generate(
            output_path=output.get_cl_docx_path(),
            letter=cl_text,
        )

        print("CL STEP 5")