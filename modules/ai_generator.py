"""
modules/ai_generator.py

AIJobAssistant
Version : v4.6.0
"""

from pathlib import Path

from modules.console import console
from modules.apply.clipboard_service import ClipboardService


class AIGenerator:

    def __init__(
        self,
    ):

        self.clipboard = ClipboardService()

    def generate_cv(
        self,
        prompt,
    ) -> str:

        return self._generate(
            "cv",
            prompt,
        )

    def generate_cl(
        self,
        prompt,
    ) -> str:

        return self._generate(
            "cover_letter",
            prompt,
        )

    def generate_analysis(
        self,
        prompt,
    ) -> str:

        return self._generate(
            "analysis",
            prompt,
        )

    def generate_detail_analysis(
        self,
        prompt,
    ) -> str:

        return self._generate(
            "detail_analysis",
            prompt,
        )

    @staticmethod
    def _normalize(
        text,
    ) -> str:

        return (
            text
            .replace(
                "\r\n",
                "\n",
            )
            .rstrip(
                "\n",
            )
        )

    def _generate(
        self,
        name,
        prompt,
    ) -> str:

        debug_dir = Path(
            "debug",
        )

        debug_dir.mkdir(
            exist_ok=True,
        )

        previous_text = self.clipboard.paste()

        self.clipboard.copy(
            prompt,
        )

        clipboard_text = self.clipboard.paste()

        (
            debug_dir
            / f"last_{name}_prompt.txt"
        ).write_text(
            clipboard_text,
            encoding="utf-8",
        )

        console.info(
            f"{name.upper()} prompt copied to clipboard."
        )

        console.info(
            f"Prompt Size : {len(prompt):,} characters"
        )

        console.info(
            f"Clipboard Size : {len(clipboard_text):,} characters"
        )

        if (
            self._normalize(
                clipboard_text,
            )
            !=
            self._normalize(
                prompt,
            )
        ):

            console.error(
                "Clipboard content differs from original prompt."
            )

            console.info(
                f"Prompt Length     : {len(prompt):,}"
            )

            console.info(
                f"Clipboard Length  : {len(clipboard_text):,}"
            )

            console.info(
                f"Length Difference : "
                f"{len(prompt) - len(clipboard_text):,}"
            )

        input(
            "\n"
            "1. Paste the prompt into ChatGPT.\n"
            "2. Copy the entire response.\n"
            "3. Press ENTER..."
        )

        response = self.clipboard.wait_changed(
            previous_text,
        )

        (
            debug_dir
            / f"last_{name}_response.txt"
        ).write_text(
            response,
            encoding="utf-8",
        )

        console.info(
            f"{name.upper()} response received."
        )

        console.info(
            f"Response Size : {len(response):,} characters"
        )

        return response.strip()

    def read_response(
        self,
    ) -> str:

        return self.clipboard.paste()