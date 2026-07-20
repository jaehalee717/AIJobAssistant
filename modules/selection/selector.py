"""
modules/selection/selector.py

AIJobAssistant
Version : v2.0.0
"""

from __future__ import annotations

from typing import Sequence, TypeVar

from .parser import SelectionParser
from .validator import SelectionValidator

T = TypeVar("T")


class Selector:
    """번호 선택 → 객체 선택."""

    @staticmethod
    def select(
        items: Sequence[T],
        selection: str,
    ) -> list[T]:

        numbers = SelectionParser.parse(
            selection
        )

        SelectionValidator.validate(
            numbers,
            len(items),
        )

        return [
            items[number - 1]
            for number in numbers
        ]