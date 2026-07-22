"""
Mail Parser
AIJobAssistant
Version : v1.0.2
"""

import re

from models.job import Job

from modules.gmail_reader import (
    get_message_body,
    get_message_html,
)
from modules.html_parser import HTMLParser


URL_PATTERN = r"https?://[^\s<>\"]+"


def parse_mail(job: Job) -> Job:

    job.body = get_message_body(
        job.message_id,
    )

    job.raw_html = get_message_html(
        job.message_id,
    )

    source = (
        job.raw_html
        if job.raw_html
        else job.body
    )

    job.description = HTMLParser.to_text(
        source,
    )

    urls = re.findall(
        URL_PATTERN,
        source,
    )

    cleaned_urls = []

    for url in urls:

        url = url.strip()

        if url.endswith("."):
            url = url[:-1]

        cleaned_urls.append(
            url,
        )

    job.urls = cleaned_urls

    job.apply_url = ""

    for url in cleaned_urls:

        lower = url.lower()

        if any(
            keyword in lower
            for keyword in (
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
            )
        ):
            job.apply_url = url
            break

    if (
        not job.apply_url
        and cleaned_urls
    ):
        job.apply_url = cleaned_urls[0]

    return job