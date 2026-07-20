"""
LinkedIn Constants
AIJobAssistant
Version : v1.5.6
"""

from pathlib import Path


PROFILE_DIR = Path("profiles") / "linkedin"

HTML_DIR = Path("output") / "linkedin"

DEFAULT_HTML = HTML_DIR / "linkedin_page.html"

PAGE_TIMEOUT = 60000

WAIT_TIMEOUT = 3000

VIEWPORT = {
    "width": 1600,
    "height": 1200,
}

SCROLL_WAIT = 1000

MAX_SCROLLS = 20

LINKEDIN_JOB_URL_PREFIXES = (
    "https://www.linkedin.com/jobs/view/",
    "https://www.linkedin.com/comm/jobs/view/",
    "https://linkedin.com/jobs/view/",
)

MAX_RETRIES = 3

RETRY_WAIT = 2000

HEADLESS = False

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/138.0.0.0 Safari/537.36"
)

LOCALE = "en-US"

TIMEZONE = "Europe/Madrid"

EXTRA_HTTP_HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
}