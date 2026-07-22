"""
modules/prompt/experience_selector.py

AIJobAssistant
Version : v2.0.0
"""


class ExperienceSelector:

    COMPANY_PRIORITY = (
        (
            (
                "education",
                "university",
                "campus",
                "student",
            ),
            "TAI",
        ),
        (
            (
                "manufacturing",
                "factory",
                "plant",
                "production",
                "warehouse",
                "supply chain",
                "logistics",
            ),
            "BRAZIL",
        ),
        (
            (
                "erp",
                "oracle",
                "gdpr",
                "service delivery",
                "infrastructure",
                "network",
                "microsoft 365",
                "azure",
                "vendor",
            ),
            "SPAIN",
        ),
        (
            (
                "bank",
                "banking",
                "escrow",
                "payment",
                "financial",
            ),
            "BANKEPOST",
        ),
        (
            (
                "ecommerce",
                "e-commerce",
                "payment gateway",
                "online",
            ),
            "LGI",
        ),
        (
            (
                "software",
                "development",
                "multimedia",
                "embedded",
                "r&d",
            ),
            "LGE",
        ),
    )

    DEFAULT_ORDER = [
        "TAI",
        "BRAZIL",
        "SPAIN",
        "BANKEPOST",
        "LGI",
        "LGE",
    ]

    @classmethod
    def build(
        cls,
        job,
    ) -> list[str]:

        jd = (
            job.description or ""
        ).lower()

        selected = []

        for keywords, company in cls.COMPANY_PRIORITY:

            if any(
                keyword in jd
                for keyword in keywords
            ):
                if company not in selected:
                    selected.append(
                        company,
                    )

        for company in cls.DEFAULT_ORDER:

            if company not in selected:
                selected.append(
                    company,
                )

        return selected

    @classmethod
    def to_text(
        cls,
        companies,
    ) -> str:

        lines = []

        lines.append(
            "=================================================="
        )

        lines.append(
            "EXPERIENCE PRIORITY"
        )

        lines.append(
            "=================================================="
        )

        lines.append(
            "Emphasize experience in this order."
        )

        for index, company in enumerate(
            companies,
            start=1,
        ):

            lines.append(
                f"{index}. {company}"
            )

        lines.append("")
        lines.append(
            "Expand the highest priority experience."
        )

        lines.append(
            "Compress lower priority experience if needed to keep the CV within two pages."
        )

        return "\n".join(
            lines,
        )