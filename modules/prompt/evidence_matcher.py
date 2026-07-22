"""
modules/prompt/evidence_matcher.py

AIJobAssistant
Version : v1.0.0
"""


class EvidenceMatcher:

    LIBRARY = {

        "Infrastructure": [
            "TAI",
            "SPAIN",
            "BRAZIL",
        ],

        "Service Delivery": [
            "TAI",
            "SPAIN",
            "BRAZIL",
        ],

        "Microsoft 365": [
            "TAI",
            "BRAZIL",
        ],

        "Azure": [
            "BRAZIL",
        ],

        "Google Workspace": [
            "TAI",
        ],

        "Oracle ERP": [
            "SPAIN",
        ],

        "GDPR": [
            "SPAIN",
        ],

        "LGPD": [
            "BRAZIL",
        ],

        "IAM": [
            "TAI",
        ],

        "SSO": [
            "TAI",
        ],

        "MFA": [
            "TAI",
        ],

        "Power BI": [
            "BRAZIL",
        ],

        "RPA": [
            "BRAZIL",
        ],

        "Manufacturing": [
            "BRAZIL",
            "SPAIN",
        ],

        "Higher Education": [
            "TAI",
        ],

        "Vendor Management": [
            "TAI",
            "SPAIN",
            "BRAZIL",
        ],

        "Information Security": [
            "TAI",
            "SPAIN",
            "BRAZIL",
        ],

    }

    @classmethod
    def build(
        cls,
        job,
    ):

        jd = (
            job.description or ""
        ).lower()

        matches = {}

        for keyword, evidence in cls.LIBRARY.items():

            if keyword.lower() in jd:

                matches[keyword] = evidence

        return matches

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
            "VERIFIED EXPERIENCE MAPPING"
        )

        lines.append(
            "=================================================="
        )

        lines.append(
            "Use ONLY the mapped experience below."
        )

        lines.append(
            "Never invent evidence."
        )

        lines.append("")

        for keyword, companies in matches.items():

            lines.append(
                f"{keyword} -> {', '.join(companies)}"
            )

        return "\n".join(
            lines,
        )