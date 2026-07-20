"""
modules/selection/validator.py

AIJobAssistant
Version : v2.0.0

Selection Validator
"""

from typing import Iterable


class SelectionValidator:
    """선택 번호 유효성 검사."""

    @staticmethod
    def validate(
        selections: Iterable[int],
        max_number: int,
    ) -> None:
        if max_number <= 0:
            raise ValueError(
                "No jobs available."
            )

        checked = set()

        for number in selections:

            if number in checked:
                raise ValueError(
                    f"Duplicate selection: {number}"
                )

            checked.add(number)

            if number < 1:
                raise ValueError(
                    f"Invalid selection: {number}"
                )

            if number > max_number:
                raise ValueError(
                    f"Selection out of range: {number}"
                )