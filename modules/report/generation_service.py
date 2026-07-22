"""
modules/report/generation_service.py

AIJobAssistant
Version : v3.0.0
"""

import hashlib
import time
from datetime import datetime
from pathlib import Path

from version import (
    CL_GENERATOR_VERSION,
    CL_PROMPT_VERSION,
    CV_GENERATOR_VERSION,
    CV_PROMPT_VERSION,
)


class GenerationService:

    @classmethod
    def start(
        cls,
    ):

        return time.perf_counter()

    @classmethod
    def finish(
        cls,
        output_dir,
        document_type,
        attempt,
        prompt,
        response,
        start_time,
        success,
        error="",
    ):

        elapsed = (
            time.perf_counter()
            - start_time
        )

        if document_type == "CV":

            prompt_version = (
                CV_PROMPT_VERSION
            )

            generator_version = (
                CV_GENERATOR_VERSION
            )

        else:

            prompt_version = (
                CL_PROMPT_VERSION
            )

            generator_version = (
                CL_GENERATOR_VERSION
            )

        cls._write_log(
            output_dir=output_dir,
            document_type=document_type,
            prompt_version=prompt_version,
            generator_version=generator_version,
            attempt=attempt,
            success=success,
            elapsed=elapsed,
            prompt=prompt,
            response=response,
            error=error,
        )

    @classmethod
    def _write_log(
        cls,
        output_dir,
        document_type,
        prompt_version,
        generator_version,
        attempt,
        success,
        elapsed,
        prompt,
        response,
        error,
    ):

        logfile = (
            Path(output_dir)
            / "generation.log"
        )

        with logfile.open(
            "a",
            encoding="utf-8",
        ) as f:

            f.write(
                "=" * 80
                + "\n"
            )

            f.write(
                f"Time               : {datetime.now():%Y-%m-%d %H:%M:%S}\n"
            )

            f.write(
                f"Document           : {document_type}\n"
            )

            f.write(
                f"Generator Version  : {generator_version}\n"
            )

            f.write(
                f"Prompt Version     : {prompt_version}\n"
            )

            f.write(
                f"Attempt            : {attempt}\n"
            )

            f.write(
                f"Success            : {success}\n"
            )

            f.write(
                f"Elapsed            : {elapsed:.2f} sec\n"
            )

            f.write(
                f"Prompt Size        : {len(prompt):,}\n"
            )

            f.write(
                f"Response Size      : {len(response):,}\n"
            )

            f.write(
                f"Prompt SHA256      : {cls.sha256(prompt)}\n"
            )

            f.write(
                f"Response SHA256    : {cls.sha256(response)}\n"
            )

            if error:

                f.write(
                    f"Error              : {error}\n"
                )

            f.write(
                "\n"
            )

    @staticmethod
    def sha256(
        text,
    ):

        return hashlib.sha256(
            text.encode(
                "utf-8",
            )
        ).hexdigest()