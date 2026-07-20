"""
Prompt Test
AIJobAssistant
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(
    0,
    str(ROOT),
)

from models.job import Job
from modules.knowledge_loader import KnowledgeLoader
from modules.prompt_builder import PromptBuilder


def main():

    knowledge = KnowledgeLoader(
        ROOT / "knowledge",
    )

    knowledge.load()

    builder = PromptBuilder(
        knowledge,
    )

    job = Job()

    job.company = "Ambition"

    job.position = "IT Director"

    job.location = "Madrid, Spain"

    job.country = "Spain"

    job.description = """
We are looking for an experienced IT Director.

Responsibilities

- IT Strategy
- Infrastructure
- Cybersecurity
- Vendor Management
- Budget
"""

    cv_prompt = builder.build_cv_prompt(
        job,
    )

    cl_prompt = builder.build_cl_prompt(
        job,
    )

    assert cv_prompt
    assert cl_prompt

    print("PASS")
    print()

    print("=" * 80)
    print("CV PROMPT")
    print("=" * 80)
    print(cv_prompt[:1000])

    print()

    print("=" * 80)
    print("CL PROMPT")
    print("=" * 80)
    print(cl_prompt[:1000])


if __name__ == "__main__":
    main()