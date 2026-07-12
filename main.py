"""
main.py
AIJobAssistant
Version : v1.1.0
"""

from config import PROJECT_ROOT
from config import DB_FILE

from utils.logger import logger

from database.db import initialize_database

from modules.gmail_auth import authenticate
from modules.gmail_reader import read_job_messages
from modules.mail_parser import parse_mail
from modules.mail_detector import detect_mail_type
from modules.job_filter import is_job_mail
from modules.job_extractor import JobExtractor
from modules.jd_parser import JDParser
from modules.score_engine import ScoreEngine
from modules.report_generator import ReportGenerator
from modules.duplicate_checker import DuplicateChecker
from modules.gmail_label_manager import GmailLabelManager


def main():

    logger.info("AIJobAssistant Started")

    initialize_database()
    logger.info("Database initialized")

    authenticate()
    logger.info("Gmail authenticated")

    report = ReportGenerator("reports")
    checker = DuplicateChecker(DB_FILE)
    label_manager = GmailLabelManager()

    print("AIJobAssistant v1.1.0")
    print(f"Project : {PROJECT_ROOT}")
    print(f"Database : {DB_FILE}")
    print()

    mails = read_job_messages()

    processed = 0
    skipped = 0
    failed = 0

    print("=" * 80)
    print(f"Found {len(mails)} mail(s)")
    print("=" * 80)

    for mail in mails:

        try:

            # Parse Mail
            mail = parse_mail(mail)

            mail.mail_type = detect_mail_type(
                mail.subject,
                mail.sender,
            ).value

            if not is_job_mail(mail):
                continue

            # One Mail -> Many Jobs
            jobs = JobExtractor.extract(mail)

            print(f"\n{mail.subject}")
            print(f"Extracted Jobs : {len(jobs)}")

            for job in jobs:

                try:

                    job = JDParser.parse(job)

                    job = ScoreEngine.evaluate(job)

                    if job.apply_url:

                        if checker.is_duplicate(job.apply_url):
                            skipped += 1
                            continue

                        checker.save(job.apply_url)

                    report_path = report.generate(job)

                    processed += 1

                    print(
                        f"[{processed}] "
                        f"{job.position} | "
                        f"{job.company} | "
                        f"{job.match} | "
                        f"{job.decision}"
                    )

                except Exception as ex:

                    failed += 1

                    print(f"Job Error : {ex}")

            # 메일 전체 처리가 끝난 후 라벨 이동
            label_manager.mark_completed(mail.message_id)

        except Exception as ex:

            failed += 1

            print()
            print("=" * 80)
            print(mail.subject)
            print(ex)
            print("=" * 80)

    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Processed : {processed}")
    print(f"Skipped   : {skipped}")
    print(f"Failed    : {failed}")


if __name__ == "__main__":
    main()