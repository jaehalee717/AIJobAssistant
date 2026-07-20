"""
Job Model
AIJobAssistant
"""

from dataclasses import dataclass, field


@dataclass
class Job:

    # Gmail
    message_id: str = ""
    thread_id: str = ""

    # Header
    subject: str = ""
    sender: str = ""
    date: str = ""

    # Portal
    portal: str = ""
    rule: str = ""

    # Mail
    body: str = ""
    raw_html: str = ""
    description: str = ""
    apply_url: str = ""
    urls: list = field(default_factory=list)
    mail_type: str = ""

    # Job
    company: str = ""
    position: str = ""

    location: str = ""

    country: str = ""
    city: str = ""
    employment_type: str = ""
    remote: str = ""
    salary: str = ""
    currency: str = ""
    language: str = ""
    visa_support: str = ""

    # AI
    match: int = 0
    confidence: str = ""
    decision: str = ""
    strength: str = ""
    weak: str = ""
    reason: str = ""

    recommendation: str = ""
    next_action: str = ""

    career_score: int = 0
    role_score: int = 0
    leadership_score: int = 0
    security_score: int = 0
    salary_score: int = 0
    location_score: int = 0
    language_score: int = 0

    total_score: int = 0