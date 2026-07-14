"""
modules/cl_generator.py
AIJobAssistant
Version : v1.5.0
"""

from __future__ import annotations

from pathlib import Path

from docx import Document


class CLGenerator:
    """Cover Letter Generator"""

    def __init__(self, template_path: Path):

        self.template_path = Path(template_path)

    def generate(
        self,
        output_path: Path,
        letter: str,
    ) -> Path:
        """
        Generate Cover Letter.

        Args:
            output_path: Output docx path
            letter: Complete cover letter text

        Returns:
            Saved docx path
        """

        document = Document(self.template_path)

        self._replace_content(
            document,
            letter,
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        document.save(output_path)

        return output_path

    def _replace_content(
        self,
        document: Document,
        text: str,
    ) -> None:

        paragraphs = document.paragraphs

        if not paragraphs:
            document.add_paragraph(text)
            return

        paragraphs[0].text = text

        for paragraph in paragraphs[1:]:
            paragraph.text = ""