"""
Mail Detector
v0.8.02

Purpose
- Detect mail source
- Decide parser
"""

from enum import Enum


class MailType(Enum):
    LINKEDIN = "LinkedIn"
    INDEED = "Indeed"
    MICHAEL_PAGE = "Michael Page"
    WORKDAY = "Workday"
    GREENHOUSE = "Greenhouse"
    LEVER = "Lever"
    SMARTRECRUITERS = "SmartRecruiters"
    COMPANY = "Company"
    UNKNOWN = "Unknown"


def detect_mail_type(subject: str, sender: str) -> MailType:

    subject = (subject or "").lower()
    sender = (sender or "").lower()

    if "linkedin" in sender:
        return MailType.LINKEDIN

    if "indeed" in sender:
        return MailType.INDEED

    if "michaelpage" in sender:
        return MailType.MICHAEL_PAGE

    if "greenhouse" in sender:
        return MailType.GREENHOUSE

    if "workday" in sender:
        return MailType.WORKDAY

    if "lever" in sender:
        return MailType.LEVER

    if "smartrecruiters" in sender:
        return MailType.SMARTRECRUITERS

    return MailType.COMPANY