"""
tests/linkedin_jd_test.py

LinkedIn JD Parser Test
AIJobAssistant v1.5.5
"""

from pathlib import Path

from modules.linkedin.jd_extractor import LinkedInJDExtractor


HTML_FILE = Path(
    "tests/linkedin_page.html",
)


def main():

    print("=" * 80)
    print("LinkedIn JD Parser Test")
    print("=" * 80)

    if not HTML_FILE.exists():

        print("HTML file not found.")
        return

    html = HTML_FILE.read_text(
        encoding="utf-8",
    )

    print(f"HTML size : {len(html)}")

    extractor = LinkedInJDExtractor()

    job = extractor.extract_from_html(
        html,
    )

    print()
    print("=" * 80)
    print("JD RESULT")
    print("=" * 80)

    print(f"Company   : {job['company']}")
    print(f"Position  : {job['position']}")
    print(f"Location  : {job['location']}")

    print()
    print("=" * 80)
    print("DESCRIPTION")
    print("=" * 80)

    print(job["description"])

    output = Path(
        "tests/linkedin_jd_result.txt",
    )

    extractor.save_job(
        job,
        output,
    )

    print()
    print("=" * 80)
    print(f"Saved : {output}")
    print("=" * 80)


if __name__ == "__main__":
    main()