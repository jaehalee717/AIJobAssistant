"""
html_parser.py
AIJobAssistant
Version : v1.0.0
"""

import re
from html import unescape


class HTMLParser:

    @staticmethod
    def to_text(html: str) -> str:

        if not html:
            return ""

        text = html

        # script
        text = re.sub(
            r"(?is)<script.*?>.*?</script>",
            " ",
            text,
        )

        # style
        text = re.sub(
            r"(?is)<style.*?>.*?</style>",
            " ",
            text,
        )

        # br
        text = re.sub(
            r"(?i)<br\s*/?>",
            "\n",
            text,
        )

        # p/div/li
        text = re.sub(
            r"(?i)</?(p|div|li|tr|table|section|article|h1|h2|h3|h4|h5|h6)[^>]*>",
            "\n",
            text,
        )

        # all tags
        text = re.sub(
            r"(?s)<[^>]+>",
            " ",
            text,
        )

        text = unescape(text)

        text = text.replace("\r", "")

        lines = []

        for line in text.split("\n"):

            line = " ".join(line.split())

            if not line:
                continue

            lines.append(line)

        return "\n".join(lines)