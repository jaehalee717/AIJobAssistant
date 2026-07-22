"""
modules/prompt/jd_strategy.py

AIJobAssistant
Version : v2.0.0
"""

from .jd_analyzer import JDAnalyzer


class JDStrategy:

    @classmethod
    def build(
        cls,
        job,
    ) -> dict:

        analysis = JDAnalyzer.analyze(
            job,
        )

        return analysis

    @classmethod
    def to_text(
        cls,
        strategy,
    ) -> str:

        lines = []

        lines.append(
            "=================================================="
        )

        lines.append(
            "JOB DESCRIPTION ANALYSIS"
        )

        lines.append(
            "=================================================="
        )

        cls._section(
            lines,
            "Required",
            strategy["required"],
        )

        cls._section(
            lines,
            "Preferred",
            strategy["preferred"],
        )

        cls._section(
            lines,
            "Responsibilities",
            strategy["responsibilities"],
        )

        cls._section(
            lines,
            "Technologies",
            strategy["technologies"],
        )

        cls._section(
            lines,
            "Leadership",
            strategy["leadership"],
        )

        cls._section(
            lines,
            "Industry",
            strategy["industry"],
        )

        cls._section(
            lines,
            "Languages",
            strategy["languages"],
        )

        cls._section(
            lines,
            "Work Model",
            strategy["work_model"],
        )

        lines.append("")
        lines.append(
            "Use this analysis to maximize recruiter confidence."
        )

        lines.append(
            "Prioritize Required over Preferred."
        )

        lines.append(
            "Do not invent missing experience."
        )

        lines.append(
            "Use only verified evidence from the Source of Truth."
        )

        return "\n".join(
            lines,
        )

    @staticmethod
    def _section(
        lines,
        title,
        values,
    ):

        if not values:
            return

        lines.append("")
        lines.append(title)

        for value in values:

            lines.append(
                f"- {value}"
            )