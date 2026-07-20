"""
LinkedIn Downloader Test
"""

from pathlib import Path

from modules.linkedin.downloader import LinkedInDownloader


TEST_URL = (
    "https://www.linkedin.com/comm/jobs/view/4439656677/"
)


def main():

    downloader = LinkedInDownloader(
        headless=False,
    )

    html = downloader.download(
        TEST_URL,
    )

    Path(
        "tests/samples/linkedin_job_page.html",
    ).write_text(
        html,
        encoding="utf-8",
    )

    print("=" * 80)
    print("HTML saved.")
    print("=" * 80)


if __name__ == "__main__":
    main()