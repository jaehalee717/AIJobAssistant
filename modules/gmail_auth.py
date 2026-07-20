"""
gmail_auth.py
AIJobAssistant
Version : v0.9.2
"""

from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from config import GMAIL_CREDENTIALS, GMAIL_TOKEN

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
]

TOKEN_FILE = GMAIL_TOKEN
CREDENTIALS_FILE = GMAIL_CREDENTIALS


def authenticate():
 
    creds = None

    # Scope가 변경되었으므로 기존 token은 무시
    if TOKEN_FILE.exists():

        try:
            creds = Credentials.from_authorized_user_file(
                TOKEN_FILE,
                SCOPES,
            )

            # 기존 token이 readonly이면 재인증
            token_scopes = set(creds.scopes or [])

            if set(SCOPES) != token_scopes:
                creds = None

        except Exception:
            creds = None

    if not creds or not creds.valid:

        if (
            creds
            and creds.expired
            and creds.refresh_token
        ):

            try:

                creds.refresh(
                    Request(),
                )

            except Exception:

                creds = None

                if TOKEN_FILE.exists():
                    TOKEN_FILE.unlink()

        else:

            # 오래된 token 삭제
            if TOKEN_FILE.exists():
                TOKEN_FILE.unlink()

            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES,
            )

            creds = flow.run_local_server(
                host="localhost",
                port=8080,
                open_browser=True,
            )

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return creds