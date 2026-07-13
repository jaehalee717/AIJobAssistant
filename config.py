"""
config.py
AIJobAssistant
Version : v0.9.0
"""

from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).parent

# System Root
SYSTEM_ROOT = Path(r"D:\InterviewSuite")

# Folders
CONFIG_DIR = SYSTEM_ROOT / "Config"
DATABASE_DIR = SYSTEM_ROOT / "Database"
LOG_DIR = SYSTEM_ROOT / "Logs"

REPORT_DIR = SYSTEM_ROOT / "Reports"
JOB_REPORT_DIR = REPORT_DIR / "JobReports"
COMPLETED_REPORT_DIR = REPORT_DIR / "Completed"
ARCHIVE_REPORT_DIR = REPORT_DIR / "Archive"

# Database
DB_FILE = DATABASE_DIR / "AIJobAssistant.db"

# Gmail Labels
JOB_LABEL = "11구직진행중/구직분석"
COMPLETED_LABEL = "11구직진행중/구직분석_완료"

# 검색 메일 갯수
#MAX_MAILS = 50    #디버깅
MAX_MAILS = 100  #실서비스
