"""
Mail Parser
AIJobAssistant
Version : v1.0.0
"""

import re

from models.job import Job

from modules.gmail_reader import get_message_body
from modules.html_parser import HTMLParser


URL_PATTERN = r"https?://[^\s<>\"]+"


def parse_mail(job: Job) -> Job:

    body = get_message_body(job.message_id)

    job.body = body

    job.description = HTMLParser.to_text(body)

    urls = re.findall(URL_PATTERN, body)

    cleaned_urls = []

    for url in urls:

        url = url.strip()

        if url.endswith("."):
            url = url[:-1]

        cleaned_urls.append(url)

    job.urls = cleaned_urls

    job.apply_url = ""

    for url in cleaned_urls:

        lower = url.lower()

        if any(keyword in lower for keyword in [
            "apply",
            "career",
            "careers",
            "job",
            "jobs",
            "position",
            "vacancy",
            "greenhouse",
            "workday",
            "lever",
            "smartrecruiters",
        ]):

            job.apply_url = url
            break

    if not job.apply_url and cleaned_urls:
        job.apply_url = cleaned_urls[0]

    return job