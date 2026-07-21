"""
modules/detail_parser.py

AIJobAssistant
Version : v2.2.1
"""

from dataclasses import dataclass


@dataclass
class DetailResult:

    recommendation: str = "N/A"
    priority: str = "N/A"

    ats_match: str = "N/A"
    interview_probability: str = "N/A"

    expected_salary: str = "N/A"

    employment_type: str = "N/A"
    work_model: str = "N/A"

    language_fit: str = "N/A"
    visa: str = "N/A"

    technical_fit: str = "N/A"
    management_fit: str = "N/A"
    leadership_fit: str = "N/A"

    can_perform: str = "N/A"

    core_strengths: str = "N/A"
    technical_gaps: str = "N/A"

    risk: str = "N/A"

    cv_focus: str = "N/A"
    cover_letter_focus: str = "N/A"

    reason: str = "N/A"

    raw_text: str = ""


class DetailParser:

    def parse(
        self,
        response: str,
    ) -> DetailResult:

        result = DetailResult(
            raw_text=response.strip(),
        )

        lines = [
            line.strip()
            for line in response.splitlines()
            if line.strip()
        ]

        mapping = {
            "recommendation": "recommendation",
            "priority": "priority",
            "estimated ats match": "ats_match",
            "interview probability": "interview_probability",
            "expected salary": "expected_salary",
            "employment type": "employment_type",
            "work model": "work_model",
            "language fit": "language_fit",
            "visa / work authorization": "visa",
            "technical fit": "technical_fit",
            "management fit": "management_fit",
            "leadership fit": "leadership_fit",
            "can perform this role": "can_perform",
            "core strengths": "core_strengths",
            "technical gaps": "technical_gaps",
            "risk": "risk",
            "cv focus": "cv_focus",
            "cover letter focus": "cover_letter_focus",
            "reason": "reason",
        }

        current_attr = None

        for line in lines:

            line = line.strip()

            # -----------------------------
            # Section Header
            # -----------------------------
            if line.startswith("●"):

                text = line.lstrip("●").strip()

                if ":" not in text:
                    continue

                key, value = text.split(
                    ":",
                    1,
                )

                key = key.strip().lower()
                value = value.strip()

                attr = mapping.get(
                    key,
                )

                if not attr:
                    current_attr = None
                    continue

                current_attr = attr

                if value:

                    if value.lower() == "unknown":
                        value = "N/A"

                    setattr(
                        result,
                        attr,
                        value,
                    )

                continue

            # -----------------------------
            # Evaluation
            # -----------------------------
            if (
                line.startswith("평가:")
                and current_attr
            ):

                value = line.replace(
                    "평가:",
                    "",
                    1,
                ).strip()

                if value:

                    setattr(
                        result,
                        current_attr,
                        value,
                    )

                continue

            # -----------------------------
            # Description
            # -----------------------------
            if (
                line.startswith("설명:")
                and current_attr
            ):

                value = line.replace(
                    "설명:",
                    "",
                    1,
                ).strip()

                if not value:
                    continue

                old = getattr(
                    result,
                    current_attr,
                )

                if old == "N/A":
                    old = ""

                if old:
                    old += "\n"

                setattr(
                    result,
                    current_attr,
                    old + value,
                )

        return result