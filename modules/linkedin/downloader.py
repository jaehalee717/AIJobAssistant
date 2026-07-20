"""
LinkedIn Downloader
AIJobAssistant
Version : v1.5.6
"""

from playwright.sync_api import sync_playwright

from modules.linkedin.constants import (
    EXTRA_HTTP_HEADERS,
    HEADLESS,
    LINKEDIN_JOB_URL_PREFIXES,
    LOCALE,
    MAX_RETRIES,
    MAX_SCROLLS,
    PAGE_TIMEOUT,
    PROFILE_DIR,
    RETRY_WAIT,
    SCROLL_WAIT,
    TIMEZONE,
    USER_AGENT,
    VIEWPORT,
    WAIT_TIMEOUT,
)

from modules.linkedin.exceptions import (
    InvalidLinkedInUrlError,
    LinkedInDownloadError,
)

from utils.logger import get_logger
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class LinkedInDownloader:

    def __init__(
        self,
        headless=HEADLESS,
    ):
        self.headless = headless
        self.logger = get_logger(__name__)

    def download(
        self,
        url: str,
    ) -> str:

        self._validate_url(
            url,
        )
      
        self.logger.info(
            f"Downloading LinkedIn JD: {url}"
        )

        PROFILE_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        with sync_playwright() as p:

            browser = p.chromium.launch_persistent_context(
                user_data_dir=str(PROFILE_DIR),
                headless=self.headless,
                viewport=VIEWPORT,
                user_agent=USER_AGENT,
                locale=LOCALE,
                timezone_id=TIMEZONE,
            )

            page = browser.new_page()

            page.set_extra_http_headers(
                EXTRA_HTTP_HEADERS,
            )

            try:

                for attempt in range(MAX_RETRIES):

                    try:

                        page.goto(
                            url,
                            wait_until="domcontentloaded",
                            timeout=PAGE_TIMEOUT,
                        )

                        break

                    except PlaywrightTimeoutError:

                        if attempt == MAX_RETRIES - 1:
                            raise

                        page.wait_for_timeout(
                            RETRY_WAIT,
                        )

                self._wait_for_login(page)

                page.wait_for_timeout(
                    WAIT_TIMEOUT,
                )

                self._scroll_page(
                    page,
                )

                html = page.content()

                if len(html) < 1000:
                    raise LinkedInDownloadError(
                        "Failed to download LinkedIn page."
                    )

                self.logger.info(
                    "LinkedIn page downloaded successfully."
                )

                return html

            except Exception as e:
                self.logger.exception(e)
                raise
            
            finally:

                browser.close()

    def _wait_for_login(
            self,
            page,
        ):

            while True:

                self.logger.info(
                    f"Current URL: {page.url}"
                )
                
                current_url = page.url.lower()

                if (
                    "login" not in current_url
                    and "checkpoint" not in current_url
                ):
                    return

                self.logger.info(
                    "Waiting for LinkedIn login..."
                )

                page.wait_for_timeout(
                    WAIT_TIMEOUT,
                )

                page.wait_for_load_state(
                    "domcontentloaded",
                )

    def _scroll_page(
        self,
        page,
    ):

        previous_height = 0

        for _ in range(MAX_SCROLLS):

            current_height = page.evaluate(
                "document.body.scrollHeight",
            )

            if current_height == previous_height:
                break

            page.evaluate(
                "window.scrollTo(0, document.body.scrollHeight)",
            )

            page.wait_for_timeout(
                1000,
            )

            previous_height = current_height

            page.evaluate(
                "window.scrollTo(0, 0)",
            )

            page.wait_for_timeout(
                SCROLL_WAIT,
            )

    def _validate_url(
        self,
        url: str,
    ):
        url = url.strip()

        if not url:
            raise ValueError(
                "LinkedIn URL is empty."
            )

        if not url.startswith(
            LINKEDIN_JOB_URL_PREFIXES,
        ):
            raise InvalidLinkedInUrlError(
                "Invalid LinkedIn Job URL."
            )