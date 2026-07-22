"""
modules/report/cv_parser.py

AIJobAssistant
Version : v6.1.0
"""


class CVParser:

    PLACEHOLDERS = (
        "title",
        "professional_profile",
        "core_competencies",
        "tai_experience",
        "brazil_title",
        "brazil_experience",
        "spain_experience",
        "bankepost_experience",
        "lgi_experience",
        "lge_experience",
    )

    @classmethod
    def parse(
        cls,
        text: str,
    ) -> dict:

        result = {
            key: ""
            for key in cls.PLACEHOLDERS
        }

        current = None

        for line in text.replace(
            "\r\n",
            "\n",
        ).split("\n"):

            line = line.strip()

            if not line:
                continue

            key = cls._parse_placeholder(
                line,
            )

            if key is not None:

                if key in result:

                    current = key

                else:

                    current = None

                continue

            if current:

                if result[current]:

                    result[current] += "\n"

                result[current] += line

        missing = [
            key
            for key, value in result.items()
            if not value.strip()
        ]

        if missing:

            raise ValueError(
                "Missing CV placeholders: "
                + ", ".join(missing)
            )

        return result

    @staticmethod
    def _parse_placeholder(
        line: str,
    ) -> str | None:

        line = line.strip()

        # {{TITLE}}
        if (
            line.startswith("{{")
            and line.endswith("}}")
        ):

            return (
                line[2:-2]
                .strip()
                .lower()
            )

        # {TITLE}
        if (
            line.startswith("{")
            and line.endswith("}")
        ):

            return (
                line[1:-1]
                .strip()
                .lower()
            )

        # TITLE:
        if line.endswith(":"):

            return (
                line[:-1]
                .strip()
                .lower()
            )

        return None