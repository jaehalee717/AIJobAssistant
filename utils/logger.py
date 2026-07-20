"""
logger.py
AIJobAssistant
Version : v1.1.0

Project logging configuration.
"""

import logging

from pathlib import Path

from config import LOG_DIR


LOG_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

LOG_FILE = LOG_DIR / "AIJobAssistant.log"


def configure_logging():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(
                LOG_FILE,
                encoding="utf-8",
            ),
            logging.StreamHandler(),
        ],
        force=True,
    )

    # ------------------------------------------------------
    # External Libraries
    # ------------------------------------------------------

    logging.getLogger(
        "googleapiclient.discovery_cache"
    ).setLevel(logging.ERROR)

    logging.getLogger(
        "googleapiclient.discovery"
    ).setLevel(logging.ERROR)

    logging.getLogger(
        "google.auth"
    ).setLevel(logging.ERROR)

    logging.getLogger(
        "google_auth_oauthlib"
    ).setLevel(logging.ERROR)

    logging.getLogger(
        "urllib3"
    ).setLevel(logging.WARNING)

    logging.getLogger(
        "requests"
    ).setLevel(logging.WARNING)


configure_logging()

def get_logger(
    name: str,
):
    return logging.getLogger(
        name,
    )

logger = logging.getLogger(
    "AIJobAssistant"
)