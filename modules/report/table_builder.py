"""
modules/report/table_builder.py

AIJobAssistant
Version : v2.0.0
"""

from __future__ import annotations

from typing import Iterable, Any


class TableBuilder:
    """Report용 테이블 데이터 생성."""

    HEADERS = [
        "No",
        "Company",
        "Position",
        "Location",
        "Score",
        "Recommendation",
    ]

    @classmethod
    def build(
        cls,
        jobs: Iterable[Any],
    ) -> tuple[list[str], list[list[str]]]:
        rows: list[list[str]] = []

        for index, job in enumerate(jobs, start=1):
            rows.append(
                [
                    str(index),
                    str(getattr(job, "company", "")),
                    str(getattr(job, "position", "")),
                    str(getattr(job, "location", "")),
                    str(getattr(job, "score", "")),
                    str(getattr(job, "recommendation", "")),
                ]
            )

        return cls.HEADERS, rows