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
from email.header import decode_header, make_header

def decode_body(data: str, charset: str | None = "utf-8") -> str:

    raw = base64.urlsafe_b64decode(data)

    for encoding in (
        charset,
        "utf-8",
        "iso-8859-1",
        "windows-1252",
    ):

        if not encoding:
            continue

        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            pass

    return raw.decode("utf-8", errors="replace")

def decode_subject(subject: str) -> str:

    if not subject:
        return ""

    try:
        decoded = decode_header(subject)
        return str(make_header(decoded))
    except Exception:
        return subject

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

                    body = decode_body(data)

                    return True

            if mime == "text/html":

                data = part.get("body", {}).get("data")

                if data:

                    body = decode_body(data)

            if "parts" in part:

                if extract(part["parts"]):
                    return True

        return False

    if "parts" in payload:

        extract(payload["parts"])

    else:

        data = payload.get("body", {}).get("data")

        if data:

            body = decode_body(data)

    return body

def get_message_html(message_id: str) -> str:

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

    def extract_html(parts):

        for part in parts:

            if part.get("mimeType") == "text/html":

                data = part.get("body", {}).get("data")

                if data:
                    return decode_body(data)

            if "parts" in part:

                html = extract_html(part["parts"])

                if html:
                    return html

        return ""

    if "parts" in payload:

        html = extract_html(payload["parts"])

        if html:
            return html

    data = payload.get("body", {}).get("data")

    if data:
        return decode_body(data)

    return ""

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
        job.subject = decode_subject(
            values.get("Subject", "")
        )
        job.sender = values.get("From", "")
        job.date = values.get("Date", "")

        jobs.append(job)

    return jobs