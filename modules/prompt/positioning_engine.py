"""
modules/prompt/positioning_engine.py

AIJobAssistant
Version : v2.1.0
"""


class PositioningEngine:

    DIRECTOR = (
        "director",
        "head",
        "regional",
        "global",
        "executive",
        "governance",
        "strategy",
        "transformation",
        "budget",
    )

    PROFESSIONAL = (
        "analyst",
        "specialist",
        "advisor",
        "consultant",
        "engineer",
        "administrator",
        "coordinator",
        "grc",
        "risk",
        "audit",
        "compliance",
    )

    INFRASTRUCTURE = (
        "infrastructure",
        "network",
        "server",
        "cloud",
        "azure",
        "vmware",
        "microsoft 365",
        "service delivery",
        "workplace",
        "endpoint",
        "telecommunication",
        "telecom",
    )

    SECURITY = (
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
    )

    MANUFACTURING = (
        "factory",
        "manufacturing",
        "production",
        "plant",
        "ot",
        "mes",
        "warehouse",
    )

    EDUCATION = (
        "education",
        "university",
        "campus",
        "student",
    )

    @classmethod
    def build(
        cls,
        job,
    ) -> dict:

        jd = (
            job.description or ""
        ).lower()

        positioning = cls._positioning(
            jd,
        )

        domains = cls._domains(
            jd,
        )

        return {
            "positioning": positioning,
            "title": cls._title(
                positioning,
                domains,
            ),
            "theme": cls._theme(
                positioning,
            ),
            "priority": cls._priority(
                positioning,
                domains,
            ),
        }

    @classmethod
    def _positioning(
        cls,
        jd,
    ):

        if any(
            x in jd
            for x in cls.DIRECTOR
        ):
            return "director"

        if any(
            x in jd
            for x in cls.PROFESSIONAL
        ):
            return "professional"

        return "manager"

    @classmethod
    def _domains(
        cls,
        jd,
    ):

        domains = []

        if any(
            x in jd
            for x in cls.INFRASTRUCTURE
        ):
            domains.append(
                "Infrastructure",
            )

        if any(
            x in jd
            for x in cls.SECURITY
        ):
            domains.append(
                "Information Security",
            )

        if any(
            x in jd
            for x in cls.MANUFACTURING
        ):
            domains.append(
                "Manufacturing IT",
            )

        if any(
            x in jd
            for x in cls.EDUCATION
        ):
            domains.append(
                "Higher Education",
            )

        if not domains:
            domains.append(
                "IT Operations",
            )

        return domains

    @classmethod
    def _title(
        cls,
        positioning,
        domains,
    ):

        if positioning == "director":

            title = [
                "IT Director",
            ]

        elif positioning == "professional":

            return (
                "Governance, Risk & Compliance (GRC)"
            )

        else:

            title = [
                "IT Operations",
            ]

        for domain in domains:

            if domain not in title:

                title.append(
                    domain,
                )

        return " | ".join(
            title[:4],
        )

    @classmethod
    def _theme(
        cls,
        positioning,
    ):

        if positioning == "director":
            return "Business Leadership"

        if positioning == "professional":
            return "Technical Excellence"

        return "Operational Excellence"

    @classmethod
    def _priority(
        cls,
        positioning,
        domains,
    ):

        priority = []

        priority.extend(
            domains,
        )

        if positioning == "director":

            priority.extend(
                [
                    "Strategy",
                    "Governance",
                    "Executive Leadership",
                    "Business Transformation",
                ]
            )

        elif positioning == "manager":

            priority.extend(
                [
                    "Service Delivery",
                    "Operations",
                    "Vendor Management",
                    "Leadership",
                ]
            )

        else:

            priority.extend(
                [
                    "Governance",
                    "Risk",
                    "Compliance",
                    "Business Support",
                ]
            )

        return priority