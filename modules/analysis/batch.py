"""
modules/analysis/batch.py

AIJobAssistant
Version : v2.0.0
"""

from __future__ import annotations

from collections.abc import Iterable

from models.job import Job
from .result import AnalysisResultParser


class AnalysisBatch:
    """여러 Job의 ChatGPT 결과 처리"""

    @staticmethod
    def parse_results(
        jobs: Iterable[Job],
        results: Iterable[str],
    ) -> list[Job]:

        parsed_jobs: list[Job] = []

        for job, result in zip(jobs, results):

            parsed_jobs.append(
                AnalysisResultParser.parse(
                    result,
                    job,
                )
            )

        return parsed_jobs