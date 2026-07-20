"""
LinkedIn Exceptions
AIJobAssistant
Version : v1.5.6
"""


class LinkedInError(Exception):
    pass


class InvalidLinkedInUrlError(LinkedInError):
    pass


class LinkedInDownloadError(LinkedInError):
    pass


class LinkedInLoginError(LinkedInError):
    pass