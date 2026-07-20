"""
modules/selection/parser.py

AIJobAssistant
Version : v2.0.0

Selection Parser

지원 형식
-----------
1
1,3,5
1-5
1,3,5-8
2-4,7,9-12
"""

from __future__ import annotations

import re
from typing import List


class SelectionParser:
    """선택 번호 문자열을 List[int]로 변환."""

    _PATTERN = re.compile(r"^\d+(?:-\d+)?$")

    @classmethod
    def parse(cls, text: str) -> List[int]:
        if not text:
            return []

        result = set()

        for token in text.split(","):
            token = token.strip()

            if not token:
                continue

            if not cls._PATTERN.fullmatch(token):
                raise ValueError(f"Invalid selection: {token}")

            if "-" in token:
                start, end = map(int, token.split("-"))

                if start > end:
                    raise ValueError(
                        f"Invalid range: {token}"
                    )

                result.update(
                    range(start, end + 1)
                )

            else:
                result.add(
                    int(token)
                )

        return sorted(result)