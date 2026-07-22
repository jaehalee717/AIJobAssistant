"""
modules/report/cv_quality_checker.py

AIJobAssistant
Version : v1.0.0
"""


class CVQualityChecker:

    @classmethod
    def validate(
        cls,
        text: str,
    ) -> None:

        cls._check_length(
            text,
        )

        cls._check_repetition(
            text,
        )

        cls._check_generic_words(
            text,
        )

    @staticmethod
    def _check_length(
        text,
    ):

        if len(text) < 4000:

            raise ValueError(
                "CV response looks too short."
            )

    @staticmethod
    def _check_repetition(
        text,
    ):

        duplicated = [
            "Responsible for",
            "Managed",
            "Supported",
            "Participated",
        ]

        for word in duplicated:

            if text.count(word) > 3:

                raise ValueError(
                    f"Too many repeated phrase : {word}"
                )

    @staticmethod
    def _check_generic_words(
        text,
    ):

        bad = [
            "hardworking",
            "passionate",
            "team player",
            "fast learner",
        ]

        lower = text.lower()

        for word in bad:

            if word in lower:

                raise ValueError(
                    f"Generic wording detected : {word}"
                )