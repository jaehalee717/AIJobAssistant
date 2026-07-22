"""
modules/report/cl_parser.py

AIJobAssistant
Version : v6.0.0
"""


class CLParser:

    PLACEHOLDERS = (
        "greeting",
        "body",
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

            if line.startswith("{{") and line.endswith("}}"):

                key = (
                    line[2:-2]
                    .strip()
                    .lower()
                )

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
                "Missing CL placeholders: "
                + ", ".join(missing)
            )

        return result