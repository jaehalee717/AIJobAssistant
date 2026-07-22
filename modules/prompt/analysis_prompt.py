"""
modules/prompt/analysis_prompt.py

AIJobAssistant
Version : v1.0.0
"""

from .common_prompt import CommonPrompt
from .job_description import JobDescription
from .output_format import OutputFormat


class AnalysisPrompt:

    @staticmethod
    def build(
        job,
        knowledge,
    ) -> str:

        return f"""
You are a senior IT recruiter and ATS evaluator.

Analyze the following job against the candidate's verified experience.

==================================================
KNOWLEDGE
==================================================

{CommonPrompt.analysis_knowledge(knowledge)}

==================================================
JOB DESCRIPTION
==================================================

{JobDescription.build(job)}

==================================================
TASKS
==================================================

1. Calculate ATS Match Score (0-100)

2. Decision
- APPLY
- REVIEW
- SKIP

3. Explain the top 5 reasons.

==================================================
OUTPUT FORMAT
==================================================

{OutputFormat.analysis()}
""".strip()