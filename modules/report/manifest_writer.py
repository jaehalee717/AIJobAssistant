"""
modules/report/manifest_writer.py

AIJobAssistant
Version : v2.0.0
"""

from datetime import datetime
from pathlib import Path

from version import (
    CL_GENERATOR_VERSION,
    CL_PROMPT_VERSION,
    CV_GENERATOR_VERSION,
    CV_PROMPT_VERSION,
    PROJECT_NAME,
    SYSTEM_VERSION,
)


class ManifestWriter:

    @classmethod
    def write(
        cls,
        output_dir,
        job,
    ) -> None:

        file = (
            Path(output_dir)
            / "manifest.txt"
        )

        file.write_text(
            cls._build(
                job,
            ),
            encoding="utf-8",
        )

    @staticmethod
    def _build(
        job,
    ) -> str:

        return f"""
==================================================
PROJECT
==================================================

Project
--------
{PROJECT_NAME}

System Version
--------
{SYSTEM_VERSION}

Generated
--------
{datetime.now():%Y-%m-%d %H:%M:%S}

==================================================
JOB INFORMATION
==================================================

Company
--------
{job.company}

Position
--------
{job.position}

Location
--------
{job.location}

Apply URL
--------
{job.apply_url}

==================================================
DOCUMENT GENERATION
==================================================

CV Prompt
--------
{CV_PROMPT_VERSION}

CV Generator
--------
{CV_GENERATOR_VERSION}

Cover Letter Prompt
--------
{CL_PROMPT_VERSION}

Cover Letter Generator
--------
{CL_GENERATOR_VERSION}
""".strip()