"""
modules/apply/clipboard_service.py

AIJobAssistant
Version : v4.0.0
"""

import time

import win32clipboard


class ClipboardService:

    @staticmethod
    def copy(
        text: str,
    ) -> None:

        win32clipboard.OpenClipboard()

        try:

            win32clipboard.EmptyClipboard()

            win32clipboard.SetClipboardData(
                win32clipboard.CF_UNICODETEXT,
                text,
            )

        finally:

            win32clipboard.CloseClipboard()

    @staticmethod
    def paste(
    ) -> str:

        win32clipboard.OpenClipboard()

        try:

            if win32clipboard.IsClipboardFormatAvailable(
                win32clipboard.CF_UNICODETEXT,
            ):

                return (
                    win32clipboard.GetClipboardData()
                    .replace("\r\n", "\n")
                    .strip()
                )

            return ""

        finally:

            win32clipboard.CloseClipboard()

    def wait_changed(
        self,
        previous_text: str,
        timeout: int = 1800,
    ) -> str:

        previous_text = (
            previous_text
            .replace("\r\n", "\n")
            .strip()
        )

        start = time.time()

        while True:

            text = self.paste()

            if text and text != previous_text:

                return text

            if time.time() - start > timeout:

                raise TimeoutError(
                    "Clipboard timeout."
                )

            time.sleep(
                1,
            )