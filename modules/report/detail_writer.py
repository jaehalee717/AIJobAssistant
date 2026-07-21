"""
modules/report/detail_writer.py

AIJobAssistant
Version : v2.2.0
"""

from docx import Document

from .table_builder import TableBuilder


class DetailWriter:
    """Detail Analysis Report 작성."""

    @staticmethod
    def write(
        document: Document,
        jobs,
    ) -> None:

        document.add_heading(
            "Detail Analysis",
            level=1,
        )

        for job in jobs:

            detail = getattr(
                job,
                "detail_result",
                None,
            )

            document.add_heading(
                f"Job No: {job.id} | {job.company} | {job.position} | {job.location}",
                level=2,
            )

            if detail is None:

                document.add_paragraph(
                    "● Detail Analysis: N/A",
                )

                continue

            document.add_paragraph( f"● Recommendation: {detail.recommendation}")
            document.add_paragraph( f"● Priority: {detail.priority}")
            document.add_paragraph( f"● Estimated ATS Match: {detail.ats_match}")
            document.add_paragraph( f"● Interview Probability: {detail.interview_probability}")
            document.add_paragraph( f"● Expected Salary: {detail.expected_salary}")
            document.add_paragraph( f"● Employment Type: {detail.employment_type}")
            document.add_paragraph( f"● Work Model: {detail.work_model}")
            document.add_paragraph( f"● Language Fit: {detail.language_fit}")
            document.add_paragraph( f"● Visa / Work Authorization: {detail.visa}")
            document.add_paragraph("● Technical Fit")
            document.add_paragraph(detail.technical_fit)
            document.add_paragraph("● Management Fit")
            document.add_paragraph(detail.management_fit)
            document.add_paragraph("● Leadership Fit")
            document.add_paragraph(detail.leadership_fit)
            document.add_paragraph("● Can Perform This Role")
            document.add_paragraph(detail.can_perform)
            document.add_paragraph("● Core Strengths")
            document.add_paragraph(detail.core_strengths)
            document.add_paragraph("● Technical Gaps")
            document.add_paragraph(detail.technical_gaps)
            document.add_paragraph("● Risk")
            document.add_paragraph(detail.risk)
            document.add_paragraph("● CV Focus")
            document.add_paragraph(detail.cv_focus)
            document.add_paragraph("● Cover Letter Focus")
            document.add_paragraph(detail.cover_letter_focus)
            document.add_paragraph("● Reason")
            document.add_paragraph(detail.reason)

            if hasattr(
                detail,
                "overall_comments",
            ):
                document.add_paragraph("● Overall Comments")
                document.add_paragraph(detail.overall_comments)