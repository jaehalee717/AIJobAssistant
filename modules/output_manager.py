"""
Output Manager

AIJobAssistant
Version : v2.1.0
"""

from datetime import datetime
from pathlib import Path

from config import OUTPUT_DIR


class OutputManager:
    """
    Create application output package folder.
    """

    CV_FILENAME = "Jaeha_Lee_CV.docx"
    CL_FILENAME = "Jaeha_Lee_CL.docx"

    # Leave some margin below Windows MAX_PATH (260)
    MAX_PATH_LENGTH = 240

    @classmethod
    def create(
        cls,
        job,
    ):

        output_dir = cls._create_output_dir(
            job,
        )

        html_file = cls._save_original_html(
            output_dir,
            job,
        )

        cv_file = output_dir / cls.CV_FILENAME

        cl_file = output_dir / cls.CL_FILENAME

        return {
            "output_dir": output_dir,
            "html_file": html_file,
            "cv_file": cv_file,
            "cl_file": cl_file,
        }

    @classmethod
    def _create_output_dir(
        cls,
        job,
    ):

        date_folder = datetime.now().strftime(
            "%Y-%m-%d"
        )

        folder_name = (
            f"{cls._clean_name(job.company)}_"
            f"{cls._clean_name(job.position)}_"
            f"{cls._clean_name(job.location)}_"
            f"{datetime.now().strftime('%Y%m%d')}"
        )

        output_dir = (
            Path(OUTPUT_DIR)
            / date_folder
            / folder_name
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        return output_dir

    @classmethod
    def _save_original_html(
        cls,
        output_dir,
        job,
    ):

        if not job.raw_html:
            return None

        company = cls._clean_name(
            job.company,
        )

        position = cls._clean_name(
            job.position,
        )

        location = cls._clean_name(
            job.location,
        )

        prefix = (
            f"{company}_{position}_"
        )

        suffix = ".html"

        current_length = (
            len(str(output_dir))
            + 1              # path separator
            + len(prefix)
            + len(suffix)
        )

        remaining = max(
            0,
            cls.MAX_PATH_LENGTH - current_length,
        )

        location = location[:remaining]

        html_name = (
            f"{prefix}"
            f"{location}"
            f"{suffix}"
        )

        html_file = output_dir / html_name

        html_file.write_text(
            job.raw_html,
            encoding="utf-8",
        )

        return html_file

    @staticmethod
    def _clean_name(
        value,
    ):

        if not value:
            return "Unknown"

        invalid_chars = [
            "<",
            ">",
            ":",
            '"',
            "/",
            "\\",
            "|",
            "?",
            "*",
        ]

        result = value

        for char in invalid_chars:
            result = result.replace(
                char,
                "_",
            )

        return result.strip()