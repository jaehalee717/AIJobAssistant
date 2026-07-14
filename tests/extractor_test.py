"""
extractor_test.py

Fast LinkedIn Extractor Test
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from modules.linkedin.extractor import LinkedInExtractor


class Mail:
    pass


def main():

    html = Path(
        "tests/linkedin_sample.html"
    ).read_text(
        encoding="utf-8",
    )

    mail = Mail()

    mail.body = html

    from modules.linkedin.parser import LinkedInParser

    lines = LinkedInParser().parse(mail.body)

    print("=" * 80)
    print(f"Lines : {len(lines)}")
    print("=" * 80)

    for line in lines[:50]:
        print(line)

    jobs = LinkedInExtractor().extract(mail)

    print("=" * 80)

    print(f"Jobs : {len(jobs)}")

    print("=" * 80)

    for i, job in enumerate(jobs, 1):

        print()

        print(f"Job {i}")

        print("-" * 50)

        print("Company :", job.company)
        print("Position:", job.position)
        print("Location:", job.location)
        print("URL     :", job.apply_url)


if __name__ == "__main__":
    main()