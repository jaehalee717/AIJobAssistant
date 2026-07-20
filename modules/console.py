"""
modules/console.py
AIJobAssistant
Version : v2.0
"""

from __future__ import annotations

import os
from colorama import Fore, Style, init

init(autoreset=True)


class Console:

    LINE = "─" * 68

    @staticmethod
    def clear() -> None:
        os.system("cls")

    @staticmethod
    def header(
        *,
        step: str,
        title: str,
        current: int,
        total: int,
    ) -> None:
        print(
            f"AIJobAssistant v2.0 | "
            f"Step {step} | "
            f"{title} | "
            f"Progress {current:02d}/{total:02d}"
        )
        print(Console.LINE)

    @staticmethod
    def job(job) -> None:

        items = [
            job.company,
            job.position,
            job.location,
        ]

        salary = getattr(job, "salary", "")

        if salary:
            items.append(salary)

        print(" | ".join(items))

    @staticmethod
    def info(text: str) -> None:
        print(text)

    @staticmethod
    def success(text: str) -> None:
        print(Fore.GREEN + text)

    @staticmethod
    def warning(text: str) -> None:
        print(Fore.YELLOW + text)

    @staticmethod
    def error(text: str) -> None:
        print(Fore.RED + text)

    @staticmethod
    def action(text: str) -> None:
        print(Fore.BLUE + f"[ACTION] {text}")

    @staticmethod
    def progress(
        current: int,
        total: int,
        width: int = 20,
    ) -> None:

        percent = int(current / total * 100)

        filled = int(width * current / total)

        bar = (
            "█" * filled +
            "░" * (width - filled)
        )

        print(
            f"Progress {current:02d}/{total:02d} | "
            f"{bar} {percent}%"
        )


console = Console()