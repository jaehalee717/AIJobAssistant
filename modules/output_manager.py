"""
modules/output_manager.py

AIJobAssistant
Version : v4.0.1
"""

import shutil
from datetime import datetime

from config import (
    CL_TEMPLATE,
    CV_TEMPLATE,
    OUTPUT_DIR,
)


class OutputManager:

    INVALID_CHARS = '\\/:*?"<>|'

    @classmethod
    def create(
        cls,
        job,
    ):

        today = datetime.now()

        date_dir = (
            OUTPUT_DIR /
            today.strftime(
                "%Y-%m-%d",
            )
        )

        folder_name = cls._sanitize(
            "_".join(
                [
                    job.company.strip(),
                    job.position.strip(),
                    job.location.strip(),
                    today.strftime(
                        "%Y%m%d",
                    ),
                ]
            )
        )

        output_dir = (
            date_dir /
            folder_name
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        cv_file = (
            output_dir /
            "Jaeha_Lee_CV.docx"
        )

        cl_file = (
            output_dir /
            "Jaeha_Lee_CL.docx"
        )

        shutil.copy2(
            CV_TEMPLATE,
            cv_file,
        )

        shutil.copy2(
            CL_TEMPLATE,
            cl_file,
        )

        cls._save_original_html(
            job,
            output_dir,
            today,
        )

        return {
            "output_dir": output_dir,
            "cv_file": cv_file,
            "cl_file": cl_file,
        }

    @classmethod
    def _save_original_html(
        cls,
        job,
        output_dir,
        today,
    ):

        html = (
            getattr(
                job,
                "raw_html",
                "",
            )
            or getattr(
                job,
                "html",
                "",
            )
        )

        if not html:
            return

        filename = cls._sanitize(
            "_".join(
                [
                    job.company.strip(),
                    job.position.strip(),
                    job.location.strip(),
                    today.strftime(
                        "%Y%m%d",
                    ),
                ]
            )
        ) + ".html"

        (
            output_dir / filename
        ).write_text(
            html,
            encoding="utf-8",
        )

    @classmethod
    def _sanitize(
        cls,
        text: str,
    ) -> str:

        for c in cls.INVALID_CHARS:
            text = text.replace(
                c,
                "_",
            )

        return text