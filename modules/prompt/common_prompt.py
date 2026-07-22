"""
modules/prompt/common_prompt.py

AIJobAssistant
Version : v2.0.0
"""

from .career_library import CareerLibrary


class CommonPrompt:

    @staticmethod
    def source_of_truth(
        knowledge,
    ) -> str:

        return f"""
==================================================
SOURCE OF TRUTH
==================================================
{knowledge.get("source_of_truth")}
""".strip()

    @staticmethod
    def career_profile(
        knowledge,
    ) -> str:

        return f"""
==================================================
CAREER PROFILE
==================================================
{knowledge.get("career_profile")}
""".strip()

    @staticmethod
    def career_evidence(
        knowledge,
    ) -> str:

        return f"""
==================================================
CAREER EVIDENCE
==================================================
{knowledge.get("career_evidence")}
""".strip()

    @staticmethod
    def career_library() -> str:

        return CareerLibrary.build()

    @staticmethod
    def ats_keywords(
        knowledge,
    ) -> str:

        return f"""
==================================================
ATS KEYWORDS
==================================================
{knowledge.get("ats_keywords")}
""".strip()

    @staticmethod
    def positioning_rules(
        knowledge,
    ) -> str:

        return f"""
==================================================
POSITIONING RULES
==================================================
{knowledge.get("positioning_rules")}
""".strip()

    @staticmethod
    def cv_rules(
        knowledge,
    ) -> str:

        return f"""
==================================================
CV WRITING RULES
==================================================
{knowledge.get("cv_rules")}
""".strip()

    @staticmethod
    def cover_letter_rules(
        knowledge,
    ) -> str:

        return f"""
==================================================
COVER LETTER WRITING RULES
==================================================
{knowledge.get("cover_letter_rules")}
""".strip()

    @staticmethod
    def analysis_knowledge(
        knowledge,
    ) -> str:

        return knowledge.get_many(
            "career_profile",
            "career_evidence",
            "analysis_rules",
            "apply_skip_rules",
        )