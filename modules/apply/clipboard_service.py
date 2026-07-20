"""
Clipboard Service
AIJobAssistant
Version : v1.5.3
"""

import time

import win32clipboard
import win32con


class ClipboardService:

    @staticmethod
    def copy(
        text: str,
    ) -> None:

        win32clipboard.OpenClipboard()

        try:

            win32clipboard.EmptyClipboard()

            win32clipboard.SetClipboardData(
                win32con.CF_UNICODETEXT,
                text,
            )

        finally:

            win32clipboard.CloseClipboard()

    @staticmethod
    def read() -> str:

        try:

            win32clipboard.OpenClipboard()

            try:

                text = win32clipboard.GetClipboardData(
                    win32con.CF_UNICODETEXT,
                )

            except TypeError:

                text = ""

            return text.strip()

        finally:

            win32clipboard.CloseClipboard()

    def wait_changed(
        self,
        expected: str,
    ) -> str:

        print()
        print("Waiting for ChatGPT response...")

        while True:

            try:

                current = self.read()

            except Exception:

                current = ""

            if (
                current
                and current != expected
            ):

                print("Clipboard changed.")

                return current

            time.sleep(1)