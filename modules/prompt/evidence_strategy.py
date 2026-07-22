"""
modules/prompt/evidence_strategy.py

AIJobAssistant
Version : v1.0.0
"""

from .evidence_matcher import EvidenceMatcher


class EvidenceStrategy:

    @classmethod
    def build(
        cls,
        job,
    ):

        return EvidenceMatcher.build(
            job,
        )

    @classmethod
    def to_text(
        cls,
        matches,
    ):

        if not matches:
            return ""

        lines = []

        lines.append(
            "=================================================="
        )

        lines.append(
            "EVIDENCE STRATEGY"
        )

        lines.append(
            "=================================================="
        )

        lines.append(
            "Every important requirement must be supported by verified experience."
        )

        lines.append(
            "Never invent evidence."
        )

        lines.append(
            "Use only the mapped experience."
        )

        lines.append("")

        for keyword, companies in matches.items():

            lines.append(
                f"{keyword}"
            )

            for company in companies:

                lines.append(
                    f"- {company}"
                )

            lines.append("")

        lines.append(
            "If no evidence exists, do NOT imply experience."
        )

        lines.append(
            "Prefer omission over exaggeration."
        )

        return "\n".join(
            lines,
        )