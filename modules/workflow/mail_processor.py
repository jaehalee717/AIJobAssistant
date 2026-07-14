"""
mail_processor.py
AIJobAssistant
Version : v1.3.2
"""

from debug import TEST_PORTAL

from modules.mail_parser import parse_mail
from modules.mail_detector import detect_mail_type
from modules.job_filter import is_job_mail
from modules.job_extractor import JobExtractor
from modules.portal_filter import detect_supported_portal


class MailProcessor:

    @classmethod
    def process(cls, mail):

        mail = parse_mail(mail)

        mail = detect_supported_portal(mail)

        if mail.portal != TEST_PORTAL:
            return []

        mail.mail_type = detect_mail_type(
            mail.subject,
            mail.sender,
        ).value

        if not is_job_mail(mail):
            return []

        return JobExtractor.extract(mail)