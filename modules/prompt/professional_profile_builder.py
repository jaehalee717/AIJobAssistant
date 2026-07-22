"""
modules/prompt/professional_profile_builder.py

AIJobAssistant
Version : v2.0.0
"""


class ProfessionalProfileBuilder:

    @classmethod
    def build(
        cls,
        job,
        strategy,
    ) -> str:

        lines = []

        lines.append(
            "=================================================="
        )

        lines.append(
            "PROFESSIONAL PROFILE STRATEGY"
        )

        lines.append(
            "=================================================="
        )

        lines.append(
            "The Professional Profile must:"
        )

        lines.append(
            "- Immediately communicate business value."
        )

        lines.append(
            "- Match the selected positioning."
        )

        lines.append(
            "- Reflect only verified experience."
        )

        lines.append(
            "- Answer why this candidate should be interviewed."
        )

        lines.append("")

        if strategy["positioning"] == "director":

            lines.extend(
                [
                    "Director Positioning",
                    "- Lead with strategy and governance.",
                    "- Emphasize executive leadership.",
                    "- Highlight international business impact.",
                    "- Keep operational details secondary.",
                ]
            )

        elif strategy["positioning"] == "manager":

            lines.extend(
                [
                    "Manager Positioning",
                    "- Lead with IT Operations.",
                    "- Emphasize Infrastructure and Service Delivery.",
                    "- Highlight vendor and stakeholder management.",
                    "- Demonstrate hands-on leadership.",
                ]
            )

        else:

            lines.extend(
                [
                    "Professional Positioning",
                    "- Lead with technical capability.",
                    "- Highlight Governance, Risk and Compliance.",
                    "- Demonstrate business support.",
                    "- Keep leadership visible but balanced.",
                ]
            )

        lines.append("")
        lines.append(
            "Maximum four concise sentences."
        )

        lines.append(
            "Avoid chronological summaries."
        )

        lines.append(
            "Avoid generic statements."
        )

        lines.append(
            "Every sentence must increase recruiter confidence."
        )

        return "\n".join(
            lines,
        )