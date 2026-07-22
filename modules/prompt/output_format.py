"""
modules/prompt/output_format.py

AIJobAssistant
Version : v1.0.0
"""

class OutputFormat:

    @staticmethod
    def cv() -> str:

        return """
Return EXACTLY in the following format.

Output EVERY placeholder exactly once.

Do NOT change any placeholder name.

Do NOT remove the curly braces.

Output the placeholder first, followed by its content.

{{TITLE}}

...

{{PROFESSIONAL_PROFILE}}

...

{{CORE_COMPETENCIES}}

...

{{TAI_EXPERIENCE}}

...

{{BRAZIL_TITLE}}

...

{{BRAZIL_EXPERIENCE}}

...

{{SPAIN_EXPERIENCE}}

...

{{BANKEPOST_EXPERIENCE}}

...

{{LGI_EXPERIENCE}}

...

{{LGE_EXPERIENCE}}

...

Rules

- Every placeholder must appear exactly once.
- Keep every placeholder exactly as written.
- Output ONLY the placeholders and their content.
- Do NOT use Markdown.
- Do NOT add explanations.
- Do NOT output any text before the first placeholder.
- Do NOT output any text after the last placeholder.
""".strip()

    @staticmethod
    def cl() -> str:

        return """
Return EXACTLY in the following format.

Output EVERY placeholder exactly once.

{{GREETING}}

...

{{BODY}}

...

Rules

- Every placeholder must appear exactly once.
- Keep every placeholder exactly as written.
- Output ONLY the placeholders and their content.
- Do NOT use Markdown.
- Do NOT add explanations.
- Do NOT output any text before the first placeholder.
- Do NOT output any text after the last placeholder.
""".strip()

    @staticmethod
    def analysis() -> str:

        return """
Return JSON only.

{
    "score": 0,
    "decision": "",
    "reason": ""
}
""".strip()

    @staticmethod
    def detail_analysis() -> str:

        return """
● Recommendation:
● Priority:
● Estimated ATS Match:
● Interview Probability:
● Expected Salary:
● Employment Type:
● Work Model:
● Language Fit:
● Visa / Work Authorization:
● Technical Fit:
평가:
설명:
● Management Fit:
평가:
설명:
● Leadership Fit:
평가:
설명:
● Can Perform This Role:
평가:
설명:
● Core Strengths:
평가:
설명:
● Technical Gaps:
평가:
설명:
● Risk:
평가:
설명:
● CV Focus:
평가:
설명:
● Cover Letter Focus:
평가:
설명:
● Reason:
평가:
설명:
● Overall Comments:
평가:
설명:
""".strip()