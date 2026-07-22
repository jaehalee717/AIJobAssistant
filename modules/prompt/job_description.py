"""
modules/prompt/job_description.py

AIJobAssistant
Version : v2.0.0
"""


class JobDescription:

    @staticmethod
    def build(
        job,
    ) -> str:

        sections = []

        if job.company:
            sections.extend(
                [
                    "Company",
                    job.company,
                    "",
                ]
            )

        if job.position:
            sections.extend(
                [
                    "Position",
                    job.position,
                    "",
                ]
            )

        if job.location:
            sections.extend(
                [
                    "Location",
                    job.location,
                    "",
                ]
            )

        if getattr(job, "salary", ""):
            sections.extend(
                [
                    "Salary",
                    job.salary,
                    "",
                ]
            )

        if getattr(job, "employment_type", ""):
            sections.extend(
                [
                    "Employment Type",
                    job.employment_type,
                    "",
                ]
            )

        if getattr(job, "remote", ""):
            sections.extend(
                [
                    "Work Style",
                    job.remote,
                    "",
                ]
            )

        if getattr(job, "language", ""):
            sections.extend(
                [
                    "Language",
                    job.language,
                    "",
                ]
            )

        sections.extend(
            [
                "Job Description",
                job.description,
            ]
        )

        return "\n".join(
            sections,
        ).strip()