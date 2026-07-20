"""
Downloader Test
"""

from modules.linkedin.downloader import LinkedInDownloader


URL = "https://www.linkedin.com/jobs/view/xxxxxxxx/"


def main():

    downloader = LinkedInDownloader(
        headless=False,
    )

    html = downloader.download(
        URL,
    )

    print(len(html))

    with open(
        "tests/samples/linkedin.html",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(html)


if __name__ == "__main__":
    main()