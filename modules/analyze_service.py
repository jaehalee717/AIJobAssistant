"""
modules/analyze_service.py
AIJobAssistant
Version : v2.0.0
"""

from database.db import initialize_database

from modules.console import console
from modules.gmail_auth import authenticate
from modules.workflow.mail_workflow import MailWorkflow
from modules.workflow.application_workflow import ApplicationWorkflow


class AnalyzeService:

    def run(
        self,
    ):

        console.clear()

        console.header(
            step="1/3",
            title="Analyze",
            current=1,
            total=3,
        )

        initialize_database()

        authenticate()

        jobs = MailWorkflow.run()

        report = ApplicationWorkflow().run(
            jobs,
        )

        console.success(
            "Analysis completed."
        )

        console.info(
            report,
        )