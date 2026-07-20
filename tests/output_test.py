"""
Output Test
AIJobAssistant
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(
    0,
    str(ROOT),
)

from models.job import Job
from modules.output_manager import OutputManager


def main():

    job = Job()

    job.company = "Ambition"
    job.position = "IT Director"
    job.country = "Spain"

    job.raw_html = """
<html>
<body>
<h1>TEST JD</h1>
</body>
</html>
"""

    output = OutputManager(
        job,
    )

    output.save_job_description(
        job.raw_html,
    )

    html_path = output.get_jd_html_path()

    assert html_path.exists()

    print("PASS")
    print(html_path)


if __name__ == "__main__":
    main()