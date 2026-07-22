"""
modules/prompt/jd_analyzer.py

AIJobAssistant
Version : v2.0.0
"""


class JDAnalyzer:

    REQUIRED = (
        "required",
        "requirements",
        "must",
        "essential",
        "qualification",
        "experience",
    )

    PREFERRED = (
        "preferred",
        "plus",
        "nice to have",
        "desirable",
        "advantage",
    )

    RESPONSIBILITY = (
        "responsibilities",
        "responsibility",
        "role",
        "key responsibilities",
        "what you will do",
    )

    TECHNOLOGIES = (
        "azure",
        "aws",
        "microsoft 365",
        "office 365",
        "google workspace",
        "vmware",
        "hyper-v",
        "oracle",
        "sap",
        "power bi",
        "rpa",
        "network",
        "server",
        "windows",
        "linux",
        "cisco",
        "iam",
        "mfa",
        "sso",
        "gdpr",
        "iso 27001",
    )

    LEADERSHIP = (
        "lead",
        "leadership",
        "manager",
        "director",
        "stakeholder",
        "vendor",
        "budget",
        "business partner",
        "cross-functional",
        "regional",
        "global",
    )

    INDUSTRY = (
        "manufacturing",
        "factory",
        "education",
        "university",
        "finance",
        "bank",
        "automotive",
        "retail",
        "logistics",
        "warehouse",
        "supply chain",
        "healthcare",
    )

    LANGUAGE = (
        "english",
        "spanish",
        "portuguese",
        "korean",
        "french",
        "german",
    )

    WORK_MODEL = (
        "remote",
        "hybrid",
        "on-site",
        "onsite",
    )

    @classmethod
    def analyze(
        cls,
        job,
    ) -> dict:

        jd = (
            job.description or ""
        )

        result = {
            "required": [],
            "preferred": [],
            "responsibilities": [],
            "technologies": [],
            "leadership": [],
            "industry": [],
            "languages": [],
            "work_model": [],
        }

        for raw in jd.splitlines():

            line = " ".join(
                raw.split()
            )

            if not line:
                continue

            lower = line.lower()

            if any(
                x in lower
                for x in cls.REQUIRED
            ):
                cls._append(
                    result["required"],
                    line,
                )

            if any(
                x in lower
                for x in cls.PREFERRED
            ):
                cls._append(
                    result["preferred"],
                    line,
                )

            if any(
                x in lower
                for x in cls.RESPONSIBILITY
            ):
                cls._append(
                    result["responsibilities"],
                    line,
                )

            for tech in cls.TECHNOLOGIES:

                if tech in lower:
                    cls._append(
                        result["technologies"],
                        tech,
                    )

            for item in cls.LEADERSHIP:

                if item in lower:
                    cls._append(
                        result["leadership"],
                        item,
                    )

            for item in cls.INDUSTRY:

                if item in lower:
                    cls._append(
                        result["industry"],
                        item,
                    )

            for item in cls.LANGUAGE:

                if item in lower:
                    cls._append(
                        result["languages"],
                        item,
                    )

            for item in cls.WORK_MODEL:

                if item in lower:
                    cls._append(
                        result["work_model"],
                        item,
                    )

        return result

    @staticmethod
    def _append(
        target,
        value,
    ):

        if value not in target:
            target.append(
                value,
            )