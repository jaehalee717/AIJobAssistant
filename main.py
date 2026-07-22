"""
main.py
AIJobAssistant
Version : v1.5.0
"""

from database.db import initialize_database

from modules.gmail_auth import authenticate
from modules.workflow.mail_workflow import MailWorkflow
from modules.workflow.application_workflow import ApplicationWorkflow

def main():

    initialize_database()

    authenticate()

    jobs = MailWorkflow.run()

    print(f"Jobs: {len(jobs)}")

    for job in jobs:
        print("=" * 80)

        print(job.company.encode("cp949", errors="replace").decode("cp949"))
        print(job.position.encode("cp949", errors="replace").decode("cp949"))
        print(job.location.encode("cp949", errors="replace").decode("cp949"))
        print(job.apply_url)

    #return

    report = ApplicationWorkflow().run(
        jobs,
    )

    print()
    print("=" * 80)
    print("Completed")
    print("=" * 80)
    print(report)


if __name__ == "__main__":
    main()