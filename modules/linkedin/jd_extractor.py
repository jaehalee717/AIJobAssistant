"""
LinkedIn JD Extractor
AIJobAssistant
Version : v1.5.6
"""

from modules.linkedin.downloader import LinkedInDownloader
from modules.linkedin.html_utils import save_html
from modules.linkedin.constants import DEFAULT_HTML
from modules.linkedin.parser import LinkedInParser


class LinkedInJDExtractor:

    def __init__(
        self,
        headless=True,
    ):
        self.downloader = LinkedInDownloader(
            headless=headless,
        )

        self.parser = LinkedInParser()

    def extract(
        self,
        url: str,
    ):

        html = self.downloader.download(
            url,
        )

        save_html(
            html,
            DEFAULT_HTML,
        )

        return self.extract_from_html(
            html,
        )

    def extract_from_html(
        self,
        html: str,
    ):

        return self.parser.parse(
            html,
        )