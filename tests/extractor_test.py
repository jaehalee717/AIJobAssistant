"""
Extractor Test
AIJobAssistant
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(
    0,
    str(ROOT),
)

from modules.linkedin.extractor import LinkedInExtractor


SAMPLE = (
    ROOT
    / "tests"
    / "samples"
    / "linkedin_job_page.html"
)


def main():

    html = SAMPLE.read_text(
        encoding="utf-8",
    )

    extractor = LinkedInExtractor()

    job = extractor.extract_html(
        html=html,
        url="https://www.linkedin.com/jobs/view/test",
    )

    assert job.company
    assert job.position
    assert job.description
    assert job.raw_html == html

    print("PASS")
    print(job.company)
    print(job.position)


if __name__ == "__main__":
    main()