"""
Job Mail Filter
"""

from models.job import Job


ALLOW_SUBJECT = [
    "application",
    "thank you for your application",
    "interview",
    "assessment",
    "invite",
    "invitation",
    "position",
    "vacancy",
    "job",
    "new jobs",
    "new job",
    "jobs posted",
    "career",
    "opportunity",
]

BLOCK_SUBJECT = [
    "newsletter",
    "weekly",
    "digest",
    "tips",
    "highlights",
    "promotion",
    "promo",
    "discount",
]

BLOCK_SENDER = [
    "nextdoor",
    "pinterest",
    "smartbrief",
    "skyscanner",
    "mediamarkt",
]


def is_job_mail(job: Job) -> bool:

    subject = job.subject.lower()
    sender = job.sender.lower()

    if job.portal == "LinkedIn Job Alerts":
        return True

    for keyword in BLOCK_SENDER:
        if keyword in sender:
            return False

    for keyword in BLOCK_SUBJECT:
        if keyword in subject:
            return False

    if job.mail_type in [
        "Workday",
        "Greenhouse",
        "Lever",
        "SmartRecruiters",
        "SuccessFactors",
    ]:
        return True

    for keyword in ALLOW_SUBJECT:
        if keyword in subject:
            return True

    return False