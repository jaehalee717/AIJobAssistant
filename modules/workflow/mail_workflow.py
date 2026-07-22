"""
mail_workflow.py
AIJobAssistant
Version : v1.5.2
"""

from modules.gmail_reader import read_job_messages
from modules.job_extractor import JobExtractor
from modules.job_filter import is_job_mail
from modules.mail_detector import detect_mail_type
from modules.mail_parser import parse_mail
from modules.portal_filter import detect_supported_portal


class MailWorkflow:

    @classmethod
    def run(cls):

        jobs = []

        mails = read_job_messages()

        for mail in mails:

            mail = parse_mail(
                mail,
            )

            mail = detect_supported_portal(
                mail,
            )

            mail.mail_type = detect_mail_type(
                mail.subject,
                mail.sender,
            ).value

            if not is_job_mail(
                mail,
            ):
                continue

            job = JobExtractor.extract(
                mail,
            )

            if not job:
                continue

            job.message_id = mail.message_id
            job.thread_id = mail.thread_id
            job.subject = mail.subject
            job.sender = mail.sender
            job.date = mail.date

            job.body = mail.body
            job.raw_html = mail.raw_html
            job.urls = mail.urls
            job.mail_type = mail.mail_type
            job.portal = mail.portal

            jobs.append(
                job,
            )

        return jobs