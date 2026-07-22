"""
modules/pdf_converter.py

AIJobAssistant
Version : v2.0.0
"""

from pathlib import Path

import win32com.client


class PDFConverter:

    def __init__(
        self,
    ):

        self.word = win32com.client.Dispatch(
            "Word.Application",
        )

        self.word.Visible = False

    def convert(
        self,
        docx_file,
    ) -> Path:

        docx_file = Path(
            docx_file,
        )

        pdf_file = docx_file.with_suffix(
            ".pdf",
        )

        document = self.word.Documents.Open(
            str(docx_file),
        )

        document.SaveAs(
            str(pdf_file),
            FileFormat=17,
        )

        document.Close(
            False,
        )

        return pdf_file

    def close(
        self,
    ) -> None:

        if self.word:

            self.word.Quit()

            self.word = None