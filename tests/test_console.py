"""
tests/test_console.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT),
)

from modules.console import Console

class DummyJob:

    company = "Microsoft"
    position = "Senior IT Infrastructure Manager"
    location = "Madrid"
    salary = "€70K"


def test_console():

    console = Console()

    console.clear()

    console.header(
        step="2/6",
        title="Detail Analysis",
        current=8,
        total=23,
    )

    console.job(DummyJob())

    console.info(
        "Analysis PASS | Recommendation APPLY | Score 91"
    )

    console.success(
        "CV Generated"
    )

    console.warning(
        "Salary not found"
    )

    console.error(
        "Clipboard Empty"
    )

    console.action(
        "ChatGPT(Ctrl+V → 응답복사) | AIJobAssistant(Ctrl+V → ENTER)"
    )

    console.progress(
        current=8,
        total=23,
    )