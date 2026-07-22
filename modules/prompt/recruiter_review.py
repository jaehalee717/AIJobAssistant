"""
modules/prompt/recruiter_review.py

AIJobAssistant
Version : v2.0.0
"""


class RecruiterReview:

    @staticmethod
    def instructions() -> str:

        return """
==================================================
RECRUITER FINAL REVIEW
==================================================

Before producing the final CV, perform one complete recruiter review.

Review the CV from the perspective of an experienced hiring manager.

Ask yourself:

1. Would I interview this candidate?

2. Does every sentence increase recruiter confidence?

3. Does every bullet provide business value?

4. Is the positioning appropriate for this Job Description?

5. Is the leadership level realistic?

6. Are ATS keywords used naturally?

7. Are there repeated achievements?

8. Are there generic responsibility statements?

9. Is there any unnecessary content?

10. Does the Professional Profile immediately communicate business value?

11. Are the strongest achievements placed first?

12. Does the CV maximize interview probability?

If any answer is NO:

• Rewrite.
• Remove weak content.
• Remove repetition.
• Improve business value.
• Improve readability.
• Keep every statement completely truthful.

Output ONLY the final recruiter-approved CV.

==================================================
"""