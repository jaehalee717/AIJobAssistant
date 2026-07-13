"""
main.py
AIJobAssistant
Version : v1.2.0
"""

from config import PROJECT_ROOT
from config import DB_FILE
from debug import TEST_PORTAL
from debug import MAX_MAILS
from debug import STOP_AFTER_FIRST_JOB
from debug import DEBUG

from utils.logger import logger

from database.db import initialize_database

from modules.gmail_auth import authenticate
from modules.gmail_reader import read_job_messages
from modules.mail_parser import parse_mail
from modules.mail_detector import detect_mail_type
from modules.job_filter import is_job_mail
from modules.job_extractor import JobExtractor
from modules.portal_filter import detect_supported_portal
from modules.jd_parser import JDParser
from modules.score_engine import ScoreEngine
from modules.report_generator import ReportGenerator
from modules.duplicate_checker import DuplicateChecker
from modules.gmail_label_manager import GmailLabelManager

def debug_print(*args, **kwargs):

    if DEBUG:
        print(*args, **kwargs)

def main():

    logger.info("AIJobAssistant Started")

    initialize_database()
    logger.info("Database initialized")

    authenticate()
    logger.info("Gmail authenticated")

    report = ReportGenerator("reports")
    checker = DuplicateChecker(DB_FILE)
    label_manager = GmailLabelManager()

    debug_print("AIJobAssistant v1.2.0")
    debug_print(f"Project : {PROJECT_ROOT}")
    debug_print(f"Database : {DB_FILE}")
    debug_print()

    mails = read_job_messages()
    if MAX_MAILS > 0:
        mails = mails[:MAX_MAILS]

    processed = 0
    skipped = 0
    failed = 0

    debug_print("=" * 80)
    debug_print(f"Found {len(mails)} mail(s)")
    debug_print("=" * 80)

    for mail in mails:

        try:

            # Parse Mail
            mail = parse_mail(mail)

            if "jobalerts-noreply@linkedin.com" not in mail.sender.lower():
                continue

            debug_print("=" * 80)
            debug_print(mail.sender)
            debug_print(mail.subject)
            debug_print("=" * 80)

            mail = detect_supported_portal(mail)

            debug_print(mail.portal)
            debug_print(mail.rule)

            if mail.portal != TEST_PORTAL:
                continue

            mail.mail_type = detect_mail_type(
                mail.subject,
                mail.sender,
            ).value

            result = is_job_mail(mail)

            if not result:
                continue

            jobs = JobExtractor.extract(mail)

            for job in jobs:

                try:

                    job = JDParser.parse(job)

                    job = ScoreEngine.evaluate(job)

                    if job.apply_url:

                        if checker.is_duplicate(job.apply_url):
                            skipped += 1
                            continue

                        checker.save(job.apply_url)

                    report.generate(job)

                    processed += 1
                    if STOP_AFTER_FIRST_JOB:
                        break

                    debug_print(
                        f"[{processed}] "
                        f"[{job.portal}] "
                        f"{job.position} | "
                        f"{job.company} | "
                        f"{job.match} | "
                        f"{job.decision}"
                    )

                except Exception as ex:

                    failed += 1

                    logger.exception(ex)

                    debug_print(f"Job Error : {ex}")

            # 메일 전체 처리가 끝난 후 라벨 이동
            label_manager.mark_completed(mail.message_id)

        except Exception as ex:

            failed += 1

            logger.exception(ex)

    report_path = report.save(
        processed=processed,
        skipped=skipped,
        failed=failed,
    )

    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Processed : {processed}")
    print(f"Skipped   : {skipped}")
    print(f"Failed    : {failed}")
    print(f"Report    : {report_path}")


if __name__ == "__main__":
    main()