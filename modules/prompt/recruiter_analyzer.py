"""
modules/prompt/recruiter_analyzer.py

AIJobAssistant
Version : v2.1.0
"""


class RecruiterAnalyzer:

    MUST_HAVE = (
        "required",
        "requirements",
        "must",
        "essential",
        "minimum",
        "qualification",
        "experience",
    )

    PREFERRED = (
        "preferred",
        "nice to have",
        "plus",
        "advantage",
        "desired",
        "desirable",
    )

    HIDDEN = (
        "stakeholder",
        "vendor",
        "communication",
        "collaboration",
        "cross-functional",
        "regional",
        "global",
        "business",
        "customer",
        "partner",
        "ownership",
        "proactive",
    )

    MAX_ITEMS = 10

    @classmethod
    def analyze(
        cls,
        job,
    ) -> dict:

        jd = (
            job.description or ""
        )

        result = {
            "must_have": [],
            "preferred": [],
            "hidden": [],
            "keywords": [],
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
                for x in cls.MUST_HAVE
            ):
                cls._append(
                    result["must_have"],
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
                for x in cls.HIDDEN
            ):
                cls._append(
                    result["hidden"],
                    line,
                )

        keywords = (
            result["must_have"]
            + result["preferred"]
            + result["hidden"]
        )

        seen = set()

        for item in keywords:

            if item in seen:
                continue

            seen.add(
                item,
            )

            result["keywords"].append(
                item,
            )

        return result

    @classmethod
    def _append(
        cls,
        target,
        value,
    ):

        if value in target:
            return

        if len(target) >= cls.MAX_ITEMS:
            return

        target.append(
            value,
        )