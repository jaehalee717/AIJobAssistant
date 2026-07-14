"""
modules/ai_generator.py
AIJobAssistant
Version : v1.5.0
"""

from __future__ import annotations

import win32clipboard
import win32con

class AIGenerator:
    """AI Prompt Generator (No API)"""

    @staticmethod
    def copy_to_clipboard(text: str) -> None:

        print(f"Clipboard text length: {len(text)}")

        win32clipboard.OpenClipboard()

        try:
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(
                win32con.CF_UNICODETEXT,
                text,
            )
        finally:
            win32clipboard.CloseClipboard()

        print("Clipboard updated.")

    def generate_cv(self, prompt: str) -> str:
        """
        Copy CV prompt to clipboard.
        """

        self.copy_to_clipboard(prompt)

        print()
        print("=" * 80)
        print("CV Prompt copied to Clipboard.")
        print("Open ChatGPT and press Ctrl + V.")
        print("=" * 80)
        print()

        return prompt

    def generate_cl(self, prompt: str) -> str:
        """
        Copy Cover Letter prompt to clipboard.
        """

        self.copy_to_clipboard(prompt)

        print()
        print("=" * 80)
        print("Cover Letter Prompt copied to Clipboard.")
        print("Open ChatGPT and press Ctrl + V.")
        print("=" * 80)
        print()

        return prompt