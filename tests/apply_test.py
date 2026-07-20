"""
Apply Test
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
from modules.apply_service import ApplyService


def main():

    service = ApplyService()

    job = Job()

    job.company = "Ambition"

    job.position = "IT Director"

    job.country = "Spain"

    job.city = "Madrid"

    job.location = "Madrid, Spain"

    job.salary = "70000"

    job.apply_url = "https://example.com"

    job.description = "Test Job Description"

    job.raw_html = """
<html>
<body>
<h1>Test</h1>
</body>
</html>
"""

    assert service.knowledge is not None
    assert service.prompt_builder is not None
    assert service.ai is not None
    assert service.cv_generator is not None
    assert service.cl_generator is not None

    print("PASS")
    print("ApplyService initialized successfully.")

    # 실제 run()은 ChatGPT 입력을 기다리므로
    # 자동 테스트에서는 호출하지 않는다.
    #
    # service.run(job)


if __name__ == "__main__":
    main()