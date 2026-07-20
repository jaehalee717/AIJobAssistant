"""
PDF Test
AIJobAssistant
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(
    0,
    str(ROOT),
)

from modules.pdf_converter import PDFConverter


def main():

    docx = (
        ROOT
        / "templates"
        / "Jaeha_Lee_CV.docx"
    )

    pdf = (
        ROOT
        / "templates"
        / "Jaeha_Lee_CV_Test.pdf"
    )

    converter = PDFConverter()

    converter.convert(
        docx,
        pdf,
    )

    converter.close()

    assert pdf.exists()

    print("PASS")
    print(pdf)


if __name__ == "__main__":
    main()