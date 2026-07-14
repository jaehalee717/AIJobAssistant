"""
mail_workflow.py
AIJobAssistant
Version : v1.5.0
"""

from modules.gmail_reader import read_job_messages
from modules.mail_parser import parse_mail
from modules.portal_filter import detect_supported_portal
from modules.mail_detector import detect_mail_type
from modules.job_filter import is_job_mail
from modules.job_extractor import JobExtractor


class MailWorkflow:

    @classmethod
    def run(cls):

        jobs = []

        mails = read_job_messages()

        for mail in mails:

            mail = parse_mail(mail)

            mail = detect_supported_portal(mail)

            mail.mail_type = detect_mail_type(
                mail.subject,
                mail.sender,
            ).value

            if not is_job_mail(mail):
                continue

            jobs.extend(
                JobExtractor.extract(mail)
            )

        return jobs