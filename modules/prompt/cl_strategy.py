"""
modules/prompt/cl_strategy.py

AIJobAssistant
Version : v3.0.0
"""

from .experience_selector import ExperienceSelector
from .positioning_engine import PositioningEngine
from .professional_profile_builder import ProfessionalProfileBuilder
from .recruiter_analyzer import RecruiterAnalyzer


class CLStrategy:

    @classmethod
    def build(
        cls,
        job,
    ) -> dict:

        positioning = PositioningEngine.build(
            job,
        )

        recruiter = RecruiterAnalyzer.analyze(
            job,
        )

        experiences = ExperienceSelector.build(
            job,
        )

        strategy = {
            "positioning": positioning["positioning"],
            "title": positioning["title"],
            "theme": positioning["theme"],
            "priority": positioning["priority"],
            "must_have": recruiter["must_have"],
            "preferred": recruiter["preferred"],
            "hidden": recruiter["hidden"],
            "experience_priority": experiences,
        }

        strategy["profile_strategy"] = (
            ProfessionalProfileBuilder.build(
                job,
                strategy,
            )
        )

        return strategy

    @classmethod
    def to_text(
        cls,
        strategy: dict,
    ) -> str:

        lines = []

        lines.append(
            "=================================================="
        )

        lines.append(
            "COVER LETTER STRATEGY"
        )

        lines.append(
            "=================================================="
        )

        lines.append(
            f"Positioning: {strategy['positioning']}"
        )

        lines.append(
            f"Title: {strategy['title']}"
        )

        lines.append(
            f"Theme: {strategy['theme']}"
        )

        lines.append("")

        lines.append(
            "Priority"
        )

        for item in strategy["priority"]:

            lines.append(
                f"- {item}"
            )

        if strategy["must_have"]:

            lines.append("")
            lines.append(
                "Must Have"
            )

            for item in strategy["must_have"]:

                lines.append(
                    f"- {item}"
                )

        if strategy["preferred"]:

            lines.append("")
            lines.append(
                "Preferred"
            )

            for item in strategy["preferred"]:

                lines.append(
                    f"- {item}"
                )

        if strategy["hidden"]:

            lines.append("")
            lines.append(
                "Hidden Requirements"
            )

            for item in strategy["hidden"]:

                lines.append(
                    f"- {item}"
                )

        lines.append("")
        lines.append(
            ExperienceSelector.to_text(
                strategy["experience_priority"],
            )
        )

        lines.append("")
        lines.append(
            strategy["profile_strategy"]
        )

        return "\n".join(
            lines,
        )