"""
gmail_label_manager.py
AIJobAssistant
Version : v0.9.0
"""

from config import JOB_LABEL
from config import COMPLETED_LABEL

from modules.gmail_service import get_gmail_service


class GmailLabelManager:

    def __init__(self):

        self.service = get_gmail_service()

    def get_label_id(self, label_name):

        results = (
            self.service.users()
            .labels()
            .list(userId="me")
            .execute()
        )

        labels = results.get("labels", [])

        for label in labels:

            if label["name"] == label_name:
                return label["id"]

        return None

    def get_job_label_id(self):

        return self.get_label_id(JOB_LABEL)

    def get_completed_label_id(self):

        return self.get_label_id(COMPLETED_LABEL)

    def mark_completed(self, message_id):

        job_label = self.get_job_label_id()
        completed_label = self.get_completed_label_id()

        if not job_label:
            return

        if not completed_label:
            return

        self.service.users().messages().modify(
            userId="me",
            id=message_id,
            body={
                "removeLabelIds": [
                    job_label
                ],
                "addLabelIds": [
                    completed_label
                ],
            },
        ).execute()