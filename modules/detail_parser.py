"""
modules/detail_parser.py
AIJobAssistant
Version : v2.0
"""

from dataclasses import dataclass


@dataclass
class DetailResult:
    apply: bool
    content: str


class DetailParser:

    def parse(
        self,
        response: str,
    ) -> DetailResult:

        text = response.strip()

        upper = text.upper()

        apply = (
            "RECOMMENDATION: APPLY" in upper
            or "RECOMMENDATION**: APPLY" in upper
            or "RECOMMENDATION = APPLY" in upper
            or "APPLY" in upper
        )

        return DetailResult(
            apply=apply,
            content=text,
        )