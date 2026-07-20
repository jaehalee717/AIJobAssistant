"""
modules/prompt_builder.py
AIJobAssistant
Version : v1.5.0
"""

from __future__ import annotations

from models.job import Job
from modules.knowledge_loader import KnowledgeLoader


class PromptBuilder:
    """Prompt Builder"""

    def __init__(
        self,
        knowledge: KnowledgeLoader,
    ):

        self.knowledge = knowledge

    def build_cv_prompt(
        self,
        job: Job,
    ) -> str:
        """
        Build CV prompt.
        """

        knowledge = self.knowledge.get_many(
            [
                "career_library",
                "cv_rules",
                "positioning_rules",
                "quality_checklist",
            ]
        )

        prompt = f"""
You are an expert ATS resume writer.

Create a professional CV for the following job.

Company:
{job.company}

Position:
{job.position}

Location:
{job.location}

Job Description:
{job.description}

Knowledge:

{knowledge}

Requirements

- Follow all CV rules.
- ATS optimized.
- Truthful only.
- Never invent experience.
- Use concise business English.
- Maximum 2 pages.
- Return only the CV content.
"""

        prompt = prompt.strip()

        print("=" * 80)
        print(f"CV Prompt Size : {len(prompt):,} chars")
        print("=" * 80)

        return prompt

    def build_cl_prompt(
        self,
        job: Job,
    ) -> str:
        """
        Build Cover Letter prompt.
        """

        knowledge = self.knowledge.get_many(
            [
                "career_library",
                "cover_letter_rules",
                "positioning_rules",
                "quality_checklist",
            ]
        )

        prompt = f"""
You are an expert cover letter writer.

Create a professional cover letter.

Company:
{job.company}

Position:
{job.position}

Location:
{job.location}

Job Description:
{job.description}

Knowledge:

{knowledge}

Requirements

- Business English.
- Professional.
- Natural.
- ATS optimized.
- Never invent experience.
- About one page.
- Return only the cover letter.
"""

        prompt = prompt.strip()

        print("=" * 80)
        print(f"CL Prompt Size : {len(prompt):,} chars")
        print("=" * 80)

        return prompt
    
    def build_analysis_prompt(
        self,
        job: Job,
    ) -> str:
        """
        Build first analysis prompt.
        """

        knowledge = self.knowledge.get_many(
            [
                "career_library",
                "apply_skip_rules",
                "positioning_rules",
                "quality_checklist",
            ]
        )

        return f"""
You are a senior IT recruiter and ATS evaluator.

Analyze the following job.

Company:
{job.company}

Position:
{job.position}

Location:
{job.location}

Job Description:
{job.description}

Knowledge:

{knowledge}

Tasks

1. Calculate ATS Match Score (0-100)

2. Decision
- APPLY
- REVIEW
- SKIP

3. Explain the top 5 reasons.

Return JSON only.

JSON Format

{{
    "score": 0,
    "decision": "",
    "reason": ""
}}
""".strip()


    def build_detail_analysis_prompt(
        self,
        job: Job,
    ) -> str:
        """
        Build detailed analysis prompt.
        """

        knowledge = self.knowledge.get_many(
            [
                "career_library",
                "apply_skip_rules",
                "positioning_rules",
                "quality_checklist",
            ]
        )

        return f"""
You are a senior IT recruiter.

Perform a detailed analysis.

Company:
{job.company}

Position:
{job.position}

Location:
{job.location}

Job Description:
{job.description}

Knowledge:

{knowledge}

Requirements

Evaluate:

- Technical Fit
- Management Fit
- Leadership Fit
- Industry Fit
- Missing Skills
- Risks
- Recommendation
- Interview Probability
- Estimated ATS Match

Return in clear Markdown.
""".strip()