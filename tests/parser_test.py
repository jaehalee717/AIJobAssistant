"""
Parser Test
"""

from pathlib import Path

from modules.linkedin.parser import LinkedInParser


def main():

    html = Path(
        "tests/samples/linkedin_job_page.html",
    ).read_text(
        encoding="utf-8",
    )

    jd = LinkedInParser.extract_jd(
        html,
    )

    print("=" * 80)
    print("Company    :", jd["company"])
    print("Position   :", jd["position"])
    print("Location   :", jd["location"])
    print("Description:", len(jd["description"]))
    print("=" * 80)
    print(jd["description"][:500])


if __name__ == "__main__":
    main()