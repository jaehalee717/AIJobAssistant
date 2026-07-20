"""
LinkedIn Extractor
AIJobAssistant
Version : v1.5.8
"""

from models.job import Job

from modules.linkedin.constants import HEADLESS
from modules.linkedin.downloader import LinkedInDownloader
from modules.linkedin.parser import LinkedInParser


class LinkedInExtractor:

    def __init__(
        self,
        headless: bool = HEADLESS,
    ):
        self.downloader = LinkedInDownloader(
            headless=headless,
        )
        self.parser = LinkedInParser()

    def extract_html(
        self,
        html: str,
        url: str = "",
    ) -> Job:

        jd = self.parser.extract_jd(
            html,
        )

        job = Job()

        job.raw_html = html
        job.apply_url = url

        job.company = jd.get(
            "company",
            "",
        )

        job.position = jd.get(
            "position",
            "",
        )

        job.location = jd.get(
            "location",
            "",
        )

        job.description = jd.get(
            "description",
            "",
        )

        if not (
            job.company
            or job.position
            or job.description
        ):
            raise ValueError(
                "Failed to parse LinkedIn page."
            )

        return job

    def extract(
        self,
        url: str,
    ) -> Job:

        html = self.downloader.download(
            url,
        )

        return self.extract_html(
            html=html,
            url=url,
        )