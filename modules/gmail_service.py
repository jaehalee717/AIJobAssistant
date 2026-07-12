from googleapiclient.discovery import build

from modules.gmail_auth import authenticate


def get_gmail_service():
    creds = authenticate()
    service = build("gmail", "v1", credentials=creds)
    return service