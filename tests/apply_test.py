"""
tests/apply_test.py

AIJobAssistant
Version : v2.3.0
"""

from modules.repository.job_repository import JobRepository
from modules.workflow.apply_workflow import ApplyWorkflow


def main():

    repository = JobRepository()

    workflow = ApplyWorkflow(
        repository,
    )

    workflow.run()


if __name__ == "__main__":

    main()