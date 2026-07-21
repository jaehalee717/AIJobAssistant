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
    
    def generate_analysis(
        self,
        prompt: str,
    ) -> str:
        """
        Copy Analysis prompt to clipboard.
        """

        self.copy_to_clipboard(prompt)

        print()
        print("=" * 80)
        print("Analysis Prompt copied to Clipboard.")
        print("Open ChatGPT and press Ctrl + V.")
        print("=" * 80)
        print()

        return prompt


    def generate_detail_analysis(
        self,
        prompt: str,
    ) -> str:
        """
        Copy Detail Analysis prompt to clipboard.
        """

        self.copy_to_clipboard(prompt)

        print()
        print("=" * 80)
        print("Detail Analysis Prompt copied to Clipboard.")
        print("Open ChatGPT and press Ctrl + V.")
        print("=" * 80)
        print()

        return prompt
    
    def read_response(self) -> str:
        """
        Read pasted AI response from console.
        Finish with Ctrl+Z then Enter (Windows).
        """

        print("Paste AI response.")
        print("Press Ctrl+Z then Enter when finished.")
        print()

        lines = []

        while True:
            try:
                line = input()
            except EOFError:
                break

            lines.append(line)

        response = "\n".join(lines).strip()

        print()
        print(f"Response length: {len(response)} characters")
        print()

        return response