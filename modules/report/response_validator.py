"""
modules/report/response_validator.py

AIJobAssistant
Version : v1.0.0
"""

import re


class ResponseValidator:

    CV_PLACEHOLDERS = (
        "TITLE",
        "PROFESSIONAL_PROFILE",
        "CORE_COMPETENCIES",
        "TAI_EXPERIENCE",
        "BRAZIL_TITLE",
        "BRAZIL_EXPERIENCE",
        "SPAIN_EXPERIENCE",
        "BANKEPOST_EXPERIENCE",
        "LGI_EXPERIENCE",
        "LGE_EXPERIENCE",
    )

    CL_PLACEHOLDERS = (
        "GREETING",
        "BODY",
    )

    @classmethod
    def validate_cv(
        cls,
        text: str,
    ):

        cls._validate(
            text,
            cls.CV_PLACEHOLDERS,
        )

    @classmethod
    def validate_cl(
        cls,
        text: str,
    ):

        cls._validate(
            text,
            cls.CL_PLACEHOLDERS,
        )

    @classmethod
    def _validate(
        cls,
        text,
        placeholders,
    ):

        cls._check_markdown(
            text,
        )

        cls._check_placeholder_count(
            text,
            placeholders,
        )

        cls._check_empty_sections(
            text,
            placeholders,
        )

    @staticmethod
    def _check_markdown(
        text,
    ):

        patterns = (
            "# ",
            "```",
            "|---",
            "**",
            "__",
        )

        for pattern in patterns:

            if pattern in text:

                raise ValueError(
                    f"Markdown detected: {pattern}"
                )

    @staticmethod
    def _check_placeholder_count(
        text,
        placeholders,
    ):

        for placeholder in placeholders:

            count = text.count(
                "{{" + placeholder + "}}"
            )

            if count != 1:

                raise ValueError(
                    f"{placeholder}: expected 1, found {count}"
                )

    @staticmethod
    def _check_empty_sections(
        text,
        placeholders,
    ):

        for index, placeholder in enumerate(
            placeholders,
        ):

            start = text.find(
                "{{" + placeholder + "}}"
            )

            if start < 0:
                continue

            start += len(
                "{{" + placeholder + "}}"
            )

            if index == len(
                placeholders,
            ) - 1:

                block = text[start:]

            else:

                next_placeholder = (
                    "{{"
                    + placeholders[index + 1]
                    + "}}"
                )

                end = text.find(
                    next_placeholder,
                    start,
                )

                block = text[
                    start:end
                ]

            if not block.strip():

                raise ValueError(
                    f"{placeholder} is empty."
                )