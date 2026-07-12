"""
JD Cleaner
v0.8.01

Purpose
- Clean Gmail Body
- Remove HTML
- Remove URL
- Remove Email
- Remove Footer
- Remove Invisible Unicode
"""

import re
import unicodedata
from html import unescape


REMOVE_PATTERNS = [
    r"Manage job alerts.*",
    r"Unsubscribe.*",
    r"Help.*",
    r"Install LinkedIn Widgets.*",
    r"Add widget.*",
    r"Learn why we included this.*",
    r"You are receiving Job Alert emails.*",
    r"Notification settings.*",
    r"Privacy Policy.*",
    r"Cookie Policy.*",
    r"Terms.*",
    r"©.*",
]


class JDCleaner:

    @staticmethod
    def clean(text: str) -> str:

        if not text:
            return ""

        text = unescape(text)

        # Normalize Unicode
        text = unicodedata.normalize("NFKC", text)

        # Remove invisible/control characters
        cleaned = []

        for ch in text:

            if unicodedata.category(ch) in (
                "Cf",
                "Cc",
            ):
                continue

            cleaned.append(ch)

        text = "".join(cleaned)

        # Remove HTML Script
        text = re.sub(
            r"<script.*?>.*?</script>",
            "",
            text,
            flags=re.I | re.S,
        )

        # Remove HTML Style
        text = re.sub(
            r"<style.*?>.*?</style>",
            "",
            text,
            flags=re.I | re.S,
        )

        # Remove HTML Tags
        text = re.sub(
            r"<[^>]+>",
            " ",
            text,
        )

        # Remove URL
        text = re.sub(
            r"http\S+",
            " ",
            text,
        )

        # Remove Email
        text = re.sub(
            r"\S+@\S+",
            " ",
            text,
        )

        lines = []

        for line in text.split("\n"):

            line = line.strip()

            if not line:
                continue

            remove = False

            for pattern in REMOVE_PATTERNS:

                if re.search(
                    pattern,
                    line,
                    re.I,
                ):
                    remove = True
                    break

            if not remove:
                lines.append(line)

        text = "\n".join(lines)

        # Remove duplicate spaces
        text = re.sub(
            r"[ \t]+",
            " ",
            text,
        )

        # Remove many blank lines
        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text,
        )

        return text.strip()