"""
Gmail Reader
AIJobAssistant
Version : v1.0.1
"""

import base64

from config import JOB_LABEL
from models.job import Job
from modules.gmail_service import get_gmail_service
from config import MAX_MAILS


def get_message_body(message_id: str) -> str:

    service = get_gmail_service()

    message = (
        service.users()
        .messages()
        .get(
            userId="me",
            id=message_id,
            format="full",
        )
        .execute()
    )

    payload = message.get("payload", {})

    body = ""

    def extract(parts):

        nonlocal body

        for part in parts:

            mime = part.get("mimeType", "")

            if mime == "text/plain":

                data = part.get("body", {}).get("data")

                if data:

                    body = base64.urlsafe_b64decode(
                        data
                    ).decode(
                        "utf-8",
                        errors="ignore",
                    )

                    return True

            if mime == "text/html":

                data = part.get("body", {}).get("data")

                if data:

                    body = base64.urlsafe_b64decode(
                        data
                    ).decode(
                        "utf-8",
                        errors="ignore",
                    )

            if "parts" in part:

                if extract(part["parts"]):
                    return True

        return False

    if "parts" in payload:

        extract(payload["parts"])

    else:

        data = payload.get("body", {}).get("data")

        if data:

            body = base64.urlsafe_b64decode(
                data
            ).decode(
                "utf-8",
                errors="ignore",
            )

    return body


def get_label_id(service, label_name):

    results = (
        service.users()
        .labels()
        .list(userId="me")
        .execute()
    )

    labels = results.get("labels", [])

    for label in labels:

        if label["name"] == label_name:
            return label["id"]

    return None


def read_job_messages():

    service = get_gmail_service()

    label_id = get_label_id(
        service,
        JOB_LABEL,
    )

    if not label_id:

        print(f"Gmail label not found : {JOB_LABEL}")

        return []

    results = (
        service.users()
        .messages()
        .list(
            userId="me",
            labelIds=[label_id],
            maxResults=MAX_MAILS,
        )
        .execute()
    )

    messages = results.get("messages", [])

    jobs = []

    for item in messages:

        message = (
            service.users()
            .messages()
            .get(
                userId="me",
                id=item["id"],
                format="metadata",
                metadataHeaders=[
                    "Subject",
                    "From",
                    "Date",
                ],
            )
            .execute()
        )

        headers = message["payload"]["headers"]

        values = {
            h["name"]: h["value"]
            for h in headers
        }

        job = Job()

        job.message_id = item["id"]
        job.thread_id = message.get("threadId", "")
        job.subject = values.get("Subject", "")
        job.sender = values.get("From", "")
        job.date = values.get("Date", "")

        jobs.append(job)

    return jobs