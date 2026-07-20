"""
modules/analysis/result.py

AIJobAssistant
Version : v2.0.0
"""

from __future__ import annotations

import json
import re

from models.job import Job


class AnalysisResultParser:
    """ChatGPT 분석 결과 Parser"""

    @staticmethod
    def parse(
        text: str,
        job: Job,
    ) -> Job:

        text = text.strip()

        match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL,
        )

        if match:

            data = json.loads(
                match.group(0)
            )

            job.match = int(
                data.get(
                    "score",
                    0,
                )
            )

            job.decision = str(
                data.get(
                    "decision",
                    "",
                )
            ).upper()

            job.reason = str(
                data.get(
                    "reason",
                    "",
                )
            )

            return job

        score = re.search(
            r"score\s*[:=]\s*(\d+)",
            text,
            re.I,
        )

        decision = re.search(
            r"decision\s*[:=]\s*([A-Z]+)",
            text,
            re.I,
        )

        reason = re.search(
            r"reason\s*[:=]\s*(.+)",
            text,
            re.I | re.S,
        )

        if score:
            job.match = int(
                score.group(1)
            )

        if decision:
            job.decision = (
                decision.group(1)
                .upper()
            )

        if reason:
            job.reason = (
                reason.group(1)
                .strip()
            )

        return job