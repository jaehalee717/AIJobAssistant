"""
modules/analyze_service.py
AIJobAssistant
Version : v1.5.0
"""

from database.db import initialize_database

from modules.gmail_auth import authenticate
from modules.workflow.mail_workflow import MailWorkflow
from modules.workflow.application_workflow import ApplicationWorkflow


class AnalyzeService:

    def run(self):

        print("=" * 80)
        print("AIJobAssistant v1.5.0")
        print("Analyze")
        print("=" * 80)

        initialize_database()

        authenticate()

        jobs = MailWorkflow.run()

        report = ApplicationWorkflow().run(jobs)

        print()
        print("=" * 80)
        print("Completed")
        print("=" * 80)
        print(report)