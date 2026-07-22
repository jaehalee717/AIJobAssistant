"""
modules/prompt/detail_analysis_prompt.py

AIJobAssistant
Version : v1.0.0
"""

from .common_prompt import CommonPrompt
from .job_description import JobDescription
from .output_format import OutputFormat


class DetailAnalysisPrompt:

    @staticmethod
    def build(
        job,
        knowledge,
    ) -> str:

        return f"""
You are a Senior IT Executive Recruiter, ATS Expert and Career Consultant.

Evaluate the following job against the candidate's verified experience.

==================================================
RULES
==================================================

- Use ONLY verified information.
- Never invent experience.
- Never invent achievements.
- Never invent technologies.
- Evaluate only against the Job Description.
- Recommendation must be APPLY, REVIEW or SKIP.
- Return ONLY the requested output.
- Do NOT use Markdown.
- Do NOT explain your methodology.

==================================================
KNOWLEDGE
==================================================

{CommonPrompt.analysis_knowledge(knowledge)}

==================================================
JOB DESCRIPTION
==================================================

{JobDescription.build(job)}

==================================================
OUTPUT FORMAT
==================================================

{OutputFormat.detail_analysis()}
""".strip()