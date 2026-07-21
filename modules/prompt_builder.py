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
You are a Senior IT Executive Recruiter, ATS Expert and Career Consultant.

Evaluate the following job against the candidate's actual experience, skills and career history.

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

Rules

- Return EXACTLY the format below.
- Keep EVERY item on ONE line.
- Do NOT insert blank lines.
- Do NOT use Markdown.
- Do NOT use tables.
- Do NOT invent experience.
- Evaluate only from the Job Description and the provided Knowledge.
- Recommendation must be APPLY, REVIEW or SKIP.
- Priority must be High, Medium or Low.
- Estimated ATS Match must be 0-100%.
- Interview Probability must contain both rating and percentage.
- Expected Salary must be Euro (€) Gross Annual Salary.
- Expected Salary should reflect the country, city, job level and current market.
- If information is unavailable, write Unknown.
- Do not explain your methodology.
- Return only the Output Format.
- For Technical Fit through Reason:
  - Write the evaluation in English after "평가:".
  - Write the explanation in Korean after "설명:".
  - The Korean explanation should be 2-4 sentences.
  - Do not translate the English evaluation.

Output Format

● Recommendation:
● Priority:
● Estimated ATS Match:
● Interview Probability:
● Expected Salary:
● Employment Type:
● Work Model:
● Language Fit:
● Visa / Work Authorization:
● Technical Fit:
평가:
설명:
● Management Fit:
평가:
설명:
● Leadership Fit:
평가:
설명:
● Can Perform This Role:
평가:
설명:
● Core Strengths:
평가:
설명:
● Technical Gaps:
평가:
설명:
● Risk:
평가:
설명:
● CV Focus:
평가:
설명:
● Cover Letter Focus:
평가:
설명:
● Reason:
평가:
설명:
● Overall Comments:
평가:
설명:
""".strip()