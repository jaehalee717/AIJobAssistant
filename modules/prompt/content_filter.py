"""
modules/prompt/content_filter.py

AIJobAssistant
Version : v1.0.0
"""


class ContentFilter:

    @staticmethod
    def instructions() -> str:

        return """
==================================================
CONTENT FILTER
==================================================

Before writing the CV:

Remove any experience that does not strengthen the target role.

Apply these rules.

1.
Remove duplicated business value.

2.
Remove duplicated technologies.

3.
Remove repeated leadership statements.

4.
Remove generic responsibilities.

Examples

Responsible for...
Managed...
Supported...
Participated in...

Rewrite them into business value whenever verified.

5.
If two bullets communicate similar value,
keep only the stronger one.

6.
Prefer relevance over chronology.

7.
Expand only the experience most relevant
to the Job Description.

8.
Compress low-value experience.

Normally compress:

• BANKePOST
• LG Internet
• LG Electronics Korea

unless the Job Description specifically
requires those industries.

9.
Do not repeat ATS keywords.

10.
Every bullet must increase interview probability.

11.
Every sentence must increase recruiter confidence.

12.
If a sentence does not improve recruiter confidence,
remove it.

13.
Maximum CV length:
Two pages.

14.
Quality is always more important than quantity.

==================================================
"""