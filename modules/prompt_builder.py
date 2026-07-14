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

    def __init__(self, knowledge: KnowledgeLoader):

        self.knowledge = knowledge

    def build_cv_prompt(
        self,
        job: Job,
    ) -> str:
        """
        Build CV prompt.
        """

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

{self.knowledge.get_all()}

Requirements

- Follow all CV rules.
- ATS optimized.
- Truthful only.
- Never invent experience.
- Use concise business English.
- Max 2 pages.
- Return only the CV content.
"""

        return prompt.strip()

    def build_cl_prompt(
        self,
        job: Job,
    ) -> str:
        """
        Build Cover Letter prompt.
        """

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

{self.knowledge.get_all()}

Requirements

- Business English.
- Professional.
- Natural.
- ATS optimized.
- Never invent experience.
- About one page.
- Return only the cover letter.
"""

        return prompt.strip()