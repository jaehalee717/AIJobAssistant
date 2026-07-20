"""
config.py
AIJobAssistant
Version : v2.0.0
"""

from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).parent

# System Root
SYSTEM_ROOT = Path(r"D:\InterviewSuite")

# Folders
# Project Config
CONFIG_DIR = PROJECT_ROOT / "config"

# System Config
SYSTEM_CONFIG_DIR = SYSTEM_ROOT / "Config"

# Gmail
GMAIL_CREDENTIALS = SYSTEM_CONFIG_DIR / "credentials.json"
GMAIL_TOKEN = SYSTEM_CONFIG_DIR / "token.json"

# AI
OPENAI_CONFIG = CONFIG_DIR / "openai.json"
DATABASE_DIR = SYSTEM_ROOT / "Database"
LOG_DIR = SYSTEM_ROOT / "Logs"

#OPENAI_CONFIG = CONFIG_DIR / "openai.json"

REPORT_DIR = SYSTEM_ROOT / "Reports"
JOB_REPORT_DIR = REPORT_DIR / "JobReports"
COMPLETED_REPORT_DIR = REPORT_DIR / "Completed"
ARCHIVE_REPORT_DIR = REPORT_DIR / "Archive"

# Output
OUTPUT_DIR = PROJECT_ROOT / "output"

# Database
DB_FILE = DATABASE_DIR / "AIJobAssistant.db"

# Gmail Labels
JOB_LABEL = "11구직진행중/구직분석"
COMPLETED_LABEL = "11구직진행중/구직분석_완료"

# 검색 메일 갯수
#MAX_MAILS = 20    #디버깅
MAX_MAILS = 100  #실서비스

# Templates
TEMPLATE_DIR = PROJECT_ROOT / "templates"

CV_TEMPLATE = TEMPLATE_DIR / "Jaeha_Lee_CV.docx"
CL_TEMPLATE = TEMPLATE_DIR / "Jaeha_Lee_CL.docx"
