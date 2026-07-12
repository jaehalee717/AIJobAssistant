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

PORTAL_RULE = {

    "LinkedIn": "LinkedInRule",

    "IrishJobs": "IrishJobsRule",

    "Indeed": "IndeedRule",

    "Michael Page": "MichaelPageRule",

    "Page Executive": "PageExecutiveRule",

    "Dennis Gorelik": "DennisGorelikRule",

    "GulfTalent": "GulfTalentRule",

    "Other": "GenericRule",

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
            job.rule = PORTAL_RULE[portal]

            return job

    job.portal = "Other"
    job.rule = PORTAL_RULE["Other"]

    return job