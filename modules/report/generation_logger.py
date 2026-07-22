"""
modules/report/generation_logger.py

AIJobAssistant
Version : v1.0.0
"""

from datetime import datetime
from pathlib import Path


class GenerationLogger:

    @classmethod
    def log(
        cls,
        output_dir,
        document_type,
        attempt,
        success,
        prompt_size,
        response_size,
        error="",
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
                f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
                f"{document_type} | "
                f"Attempt={attempt} | "
                f"Success={success} | "
                f"Prompt={prompt_size} | "
                f"Response={response_size}"
            )

            if error:

                f.write(
                    f" | Error={error}"
                )

            f.write("\n")