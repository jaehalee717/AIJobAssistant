"""
modules/linkedin/constants.py

LinkedIn Constants
Version : v1.2.0
"""

from __future__ import annotations

import re

PORTAL_NAME = "LinkedIn Job Alerts"

FIELD_COUNT = 3

POSITION_INDEX = 2
COMPANY_INDEX = 1
LOCATION_INDEX = 0
VIEW_JOB_PREFIX = "View job:"

IGNORE_LINES = {
    "",
    "Fast growing",
    "Top applicant",
    "Apply with resume & profile",
    "This company is actively hiring",
}

URL_PATTERN = re.compile(
    r"^View job:\s*(https://\S+)",
    re.IGNORECASE,
)