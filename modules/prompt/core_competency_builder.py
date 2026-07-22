"""
modules/prompt/core_competency_builder.py

AIJobAssistant
Version : v2.0.0
"""


class CoreCompetencyBuilder:

    COMPETENCIES = {
        "Infrastructure & Cloud": (
            "infrastructure",
            "network",
            "server",
            "cloud",
            "azure",
            "vmware",
            "microsoft 365",
            "endpoint",
            "service delivery",
        ),
        "Information Security": (
            "security",
            "cyber",
            "iso 27001",
            "gdpr",
            "lgpd",
            "iam",
            "mfa",
            "sso",
            "risk",
            "compliance",
        ),
        "Enterprise Applications": (
            "erp",
            "oracle",
            "power bi",
            "rpa",
            "application",
        ),
        "Leadership & Governance": (
            "leadership",
            "stakeholder",
            "vendor",
            "governance",
            "budget",
            "project",
        ),
        "Operations & ITSM": (
            "operations",
            "itil",
            "itsm",
            "support",
            "helpdesk",
            "incident",
            "service",
        ),
        "Digital Transformation": (
            "digital",
            "transformation",
            "automation",
            "process",
            "improvement",
        ),
    }

    @classmethod
    def build(
        cls,
        job,
    ) -> list[str]:

        jd = (
            job.description or ""
        ).lower()

        selected = []

        for category, keywords in cls.COMPETENCIES.items():

            if any(
                keyword in jd
                for keyword in keywords
            ):
                selected.append(
                    category,
                )

        if not selected:

            selected = [
                "Infrastructure & Cloud",
                "Information Security",
                "Leadership & Governance",
            ]

        return selected[:6]

    @classmethod
    def to_text(
        cls,
        competencies,
    ) -> str:

        lines = []

        lines.append(
            "=================================================="
        )

        lines.append(
            "CORE COMPETENCY STRATEGY"
        )

        lines.append(
            "=================================================="
        )

        lines.append(
            "Prioritize these competency categories."
        )

        for index, category in enumerate(
            competencies,
            start=1,
        ):
            lines.append(
                f"{index}. {category}"
            )

        lines.append("")
        lines.append(
            "Generate no more than six Core Competency bullets."
        )

        lines.append(
            "Group ATS keywords naturally under each business category."
        )

        lines.append(
            "Avoid keyword stuffing."
        )

        return "\n".join(
            lines,
        )