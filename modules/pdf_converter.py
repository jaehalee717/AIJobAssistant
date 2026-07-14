"""
modules/pdf_converter.py
AIJobAssistant
Version : v1.5.0
"""

from __future__ import annotations

from pathlib import Path

import win32com.client


class PDFConverter:
    """Word DOCX -> PDF Converter"""

    def __init__(self):

        self.word = win32com.client.Dispatch("Word.Application")
        self.word.Visible = False

    def convert(
        self,
        docx_path: Path,
        pdf_path: Path,
    ) -> Path:
        """
        Convert DOCX to PDF.

        Args:
            docx_path: Source DOCX
            pdf_path: Target PDF

        Returns:
            PDF path
        """

        docx_path = Path(docx_path)
        pdf_path = Path(pdf_path)

        pdf_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        document = self.word.Documents.Open(str(docx_path))

        document.SaveAs(
            str(pdf_path),
            FileFormat=17,      # wdFormatPDF
        )

        document.Close(False)

        return pdf_path

    def close(self) -> None:
        """Close Word"""

        if self.word:
            self.word.Quit()