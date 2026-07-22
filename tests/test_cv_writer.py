"""
tests/test_cv_writer.py

AIJobAssistant
Version : v5.0.0
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT),
)

from config import (
    CV_TEMPLATE,
    OUTPUT_DIR,
)

from modules.report.cv_writer import CVWriter


AI_TEXT = """
{{ title }}
TEST TITLE

{{ professional_profile }}
A & B # C ^ D @ E

{{ core_competencies }}
• IT Strategy & Governance
• Infrastructure & Cloud
• Risk & Compliance

{{ tai_experience }}
• Test

{{ brazil_title }}
Senior Manager – IT & Information Security & General Affairs

{{ brazil_experience }}
• Implemented LGPD governance across the organization.
• Delivered Azure and Microsoft 365 modernization.

{{ spain_experience }}
• Led Oracle ERP rollout.
• Improved GDPR compliance.

{{ bankepost_experience }}
• Led development and delivery of secure payment systems leveraging banking escrow platforms.

{{ lgi_experience }}
• Managed mission-critical eCommerce operations.
• Built payment gateway platforms.

{{ lge_experience }}
• Developed flowchart-based automation tool for multimedia systems.
"""


def main():

    OUTPUT_DIR.mkdir(
        exist_ok=True,
    )

    output = OUTPUT_DIR / "CV_Test.docx"

    CVWriter.write(
        template=CV_TEMPLATE,
        output=output,
        ai_text=AI_TEXT,
    )

    print()
    print(output)
    print()
    print("CV Writer Test OK")


if __name__ == "__main__":
    main()