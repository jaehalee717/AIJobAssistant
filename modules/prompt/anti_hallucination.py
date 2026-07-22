"""
modules/prompt/anti_hallucination.py

AIJobAssistant
Version : v1.0.0
"""


class AntiHallucination:

    @staticmethod
    def instructions() -> str:

        return """
==================================================
ANTI-HALLUCINATION RULES
==================================================

Every statement must be supported by verified evidence.

Never:

- invent experience
- invent achievements
- invent technologies
- invent certifications
- invent leadership
- invent budgets
- invent project scope
- invent team size
- invent KPIs
- invent percentages
- invent business impact

If the Job Description requests something that is not verified:

- do not imply experience
- do not exaggerate
- do not infer
- do not estimate

Instead:

- emphasize transferable experience
- use the closest verified evidence
- remain completely truthful

Truthfulness has higher priority than ATS optimization.

==================================================
""".strip()