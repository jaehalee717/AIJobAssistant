"""
tests/test_cl_writer.py

AIJobAssistant
Version : v5.0.0
"""

from config import (
    CL_TEMPLATE,
    OUTPUT_DIR,
)

from modules.report.cl_writer import CLWriter


AI_TEXT = """
{{ greeting }}
Dear Hiring Manager,

{{ body }}
I am excited to apply for this position.

With more than 30 years of international experience in IT leadership, Information Security and Governance, I have led digital transformation, cybersecurity, cloud migration and enterprise IT initiatives across Europe, Latin America and Asia.

I believe my experience in business-focused IT leadership, governance and stakeholder management aligns well with the requirements of this role.

Thank you for your time and consideration. I look forward to discussing how I can contribute to your organization.
"""


def main():

    OUTPUT_DIR.mkdir(
        exist_ok=True,
    )

    output = OUTPUT_DIR / "CL_Test.docx"

    CLWriter.write(
        template=CL_TEMPLATE,
        output=output,
        ai_text=AI_TEXT,
    )

    print()
    print(output)
    print()
    print("CL Writer Test OK")


if __name__ == "__main__":
    main()