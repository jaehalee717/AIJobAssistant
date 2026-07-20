"""
LinkedIn HTML Utils
AIJobAssistant
Version : v1.5.6
"""

from pathlib import Path


def save_html(
    html: str,
    path: Path,
):

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    path.write_text(
        html,
        encoding="utf-8",
    )


def load_html(
    path: Path,
) -> str:

    return path.read_text(
        encoding="utf-8",
    )