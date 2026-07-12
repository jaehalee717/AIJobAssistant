"""
portal_filter.py
AIJobAssistant
Version : v1.1
"""

SUPPORTED_PORTALS = {

    "linkedin": "LinkedIn",

    "irishjobs": "IrishJobs",

    "indeed": "Indeed",

    "michael page": "Michael Page",

    "page executive": "Page Executive",

    "dennis gorelik": "Dennis Gorelik",

    "gulftalent": "GulfTalent",

}


def detect_supported_portal(job):

    text = (
        f"{job.subject} "
        f"{job.sender} "
        f"{job.body}"
    ).lower()

    for keyword, portal in SUPPORTED_PORTALS.items():

        if keyword in text:

            job.portal = portal
            return True

    job.portal = "Other"

    return False