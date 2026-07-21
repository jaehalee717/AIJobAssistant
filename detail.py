"""
detail.py
AIJobAssistant
Version : v2.2.0
"""

from database.db import initialize_database

from modules.gmail_auth import authenticate
from modules.detail_service import DetailService


def main():

    initialize_database()

    authenticate()

    DetailService().run()


if __name__ == "__main__":
    main()