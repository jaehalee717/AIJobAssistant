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

    # Mail
    body: str = ""
    description: str = ""
    apply_url: str = ""
    urls: list = field(default_factory=list)
    mail_type: str = ""

    # Job
    company: str = ""
    position: str = ""
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