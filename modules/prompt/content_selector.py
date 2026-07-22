"""
modules/prompt/content_selector.py

AIJobAssistant
Version : v1.0.0
"""


class ContentSelector:

    RULES = {

        "azure": (
            "BRAZIL",
        ),

        "microsoft 365": (
            "BRAZIL",
            "TAI",
        ),

        "google workspace": (
            "TAI",
        ),

        "oracle": (
            "SPAIN",
        ),

        "erp": (
            "SPAIN",
        ),

        "gdpr": (
            "SPAIN",
        ),

        "lgpd": (
            "BRAZIL",
        ),

        "iam": (
            "TAI",
        ),

        "sso": (
            "TAI",
        ),

        "mfa": (
            "TAI",
        ),

        "power bi": (
            "BRAZIL",
        ),

        "rpa": (
            "BRAZIL",
        ),

        "manufacturing": (
            "BRAZIL",
            "SPAIN",
        ),

        "factory": (
            "BRAZIL",
            "SPAIN",
        ),

        "higher education": (
            "TAI",
        ),

        "vendor": (
            "TAI",
            "BRAZIL",
            "SPAIN",
        ),

        "service delivery": (
            "TAI",
            "SPAIN",
            "BRAZIL",
        ),

        "infrastructure": (
            "TAI",
            "SPAIN",
            "BRAZIL",
        ),

        "information security": (
            "TAI",
            "SPAIN",
            "BRAZIL",
        ),
    }

    @classmethod
    def build(
        cls,
        job,
    ):

        jd = (
            job.description or ""
        ).lower()

        selected = {}

        for keyword, evidence in cls.RULES.items():

            if keyword in jd:

                selected[keyword] = list(
                    evidence,
                )

        return selected

    @classmethod
    def to_text(
        cls,
        selected,
    ):

        if not selected:
            return ""

        lines = []

        lines.append(
            "=================================================="
        )

        lines.append(
            "CONTENT SELECTION"
        )

        lines.append(
            "=================================================="
        )

        lines.append(
            "Prioritize the following verified evidence."
        )

        lines.append("")

        for keyword, companies in selected.items():

            lines.append(
                f"{keyword}"
            )

            for company in companies:

                lines.append(
                    f"  - {company}"
                )

        lines.append("")

        lines.append(
            "Do NOT use unrelated experience."
        )

        lines.append(
            "Do NOT repeat similar evidence."
        )

        lines.append(
            "Select the strongest evidence only."
        )

        return "\n".join(
            lines,
        )