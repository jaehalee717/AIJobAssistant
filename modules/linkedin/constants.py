"""
modules/linkedin/constants.py

LinkedIn Constants
Version : v1.2.0
"""

from __future__ import annotations

import re

PORTAL_NAME = "LinkedIn Job Alerts"

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