"""
Apply Flow Test
AIJobAssistant
"""

import sys
from pathlib import Path

print("TEST STEP 1")

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT),
)

print("TEST STEP 2")

from models.job import Job

print("TEST STEP 3")

from modules.apply_service import ApplyService

print("TEST STEP 4")


def main():

    print("TEST STEP 5")

    job = Job()

    job.company = "EA"
    job.position = "First Systems Operations Manager"

    job.country = "Spain"
    job.city = "Madrid"
    job.location = "Madrid, Spain"

    job.salary = "70000"

    job.apply_url = "https://example.com"

    job.description = "Test"

    job.raw_html = "<html></html>"

    print("TEST STEP 6")

    ApplyService().run(job)

    print("TEST STEP 7")


if __name__ == "__main__":

    print("TEST STEP 8")

    main()

    print("TEST STEP 9")