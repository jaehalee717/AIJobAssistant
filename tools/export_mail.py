"""
tools/export_mail.py

Export one Gmail message to tests/linkedin_sample.html

Version : v1.0.0
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from modules.gmail_auth import authenticate
from modules.gmail_service import get_gmail_service
from modules.gmail_reader import (
    get_label_id,
    get_message_html,
)
from config import JOB_LABEL

DEBUG_INDEX = 6

OUTPUT = Path("tests/linkedin_sample.html")


def main():

    authenticate()

    service = get_gmail_service()

    label_id = get_label_id(
        service,
        JOB_LABEL,
    )

    if not label_id:
        print("Label not found.")
        return

    results = (
        service.users()
        .messages()
        .list(
            userId="me",
            labelIds=[label_id],
            maxResults=20,
        )
        .execute()
    )

    messages = results.get("messages", [])

    if not messages:
        print("No messages.")
        return

    print()
    print("=" * 80)

    for i, msg in enumerate(messages, 1):

        metadata = (
            service.users()
            .messages()
            .get(
                userId="me",
                id=msg["id"],
                format="metadata",
                metadataHeaders=[
                    "Subject",
                    "From",
                ],
            )
            .execute()
        )

        subject = ""
        sender = ""

        for h in metadata["payload"]["headers"]:

            if h["name"] == "Subject":
                subject = h["value"]

            elif h["name"] == "From":
                sender = h["value"]

        sender = sender.split("<")[0].strip()

        print(f"{i:2d}. [{sender[:15]:15}] {subject[:90]}")

    print("=" * 80)

    print()
    index = DEBUG_INDEX

    if index < 0 or index >= len(messages):
        print("Invalid.")
        return

    html = get_message_html(
        messages[index]["id"]
    )

    OUTPUT.write_text(
        html,
        encoding="utf-8",
    )

    print()
    print("Saved")
    print(OUTPUT)


if __name__ == "__main__":
    main()