"""
Extractor Test
"""

from modules.linkedin.extractor import LinkedInExtractor

TEST_URL = (
    "https://www.linkedin.com/comm/jobs/view/4439656677/"
)

def main():

    job = LinkedInExtractor(
        headless=False,
    ).extract(
        URL,
    )

    print("=" * 80)
    print("Company   :", job.company)
    print("Position  :", job.position)
    print("Location  :", job.location)
    print("Description")
    print("-" * 80)
    print(job.description[:300])


if __name__ == "__main__":
    main()