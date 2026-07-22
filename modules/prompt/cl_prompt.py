"""
modules/prompt/cl_prompt.py

AIJobAssistant
Version : v3.1.0
"""

from .anti_hallucination import AntiHallucination
from .cl_strategy import CLStrategy
from .common_prompt import CommonPrompt
from .content_filter import ContentFilter
from .evidence_strategy import EvidenceStrategy
from .jd_strategy import JDStrategy
from .job_description import JobDescription
from .output_format import OutputFormat
from .recruiter_decision_engine import RecruiterDecisionEngine
from .recruiter_review import RecruiterReview


class CLPrompt:

    @staticmethod
    def build(
        job,
        knowledge,
    ) -> str:

        cl_strategy = CLStrategy.build(
            job,
        )

        cl_strategy_text = CLStrategy.to_text(
            cl_strategy,
        )

        jd_strategy = JDStrategy.build(
            job,
        )

        jd_strategy_text = JDStrategy.to_text(
            jd_strategy,
        )

        evidence = EvidenceStrategy.build(
            job,
        )

        evidence_text = EvidenceStrategy.to_text(
            evidence,
        )

        content_filter = (
            ContentFilter.instructions()
        )

        anti_hallucination = (
            AntiHallucination.instructions()
        )

        recruiter_decision = (
            RecruiterDecisionEngine.instructions()
        )

        recruiter_review = (
            RecruiterReview.instructions()
        )

        return f"""
You are an expert Executive Cover Letter Writer.

Your objective is NOT simply to write a cover letter.

Your objective is to maximize:

• Interview Probability
• Recruiter Confidence
• Hiring Probability

while remaining completely truthful.

==================================================
ABSOLUTE RULES
==================================================

- Use ONLY verified information.
- Never invent experience.
- Never invent achievements.
- Never invent technologies.
- Never invent leadership.
- Never exaggerate seniority.
- Tailor only verified experience.
- Every important requirement must be supported by verified evidence.
- If verified evidence does not exist, omit it.
- Preserve factual accuracy.
- Do NOT copy the Job Description.
- Maintain a professional executive tone.
- Do NOT use Markdown.
- Do NOT explain your reasoning.
- Output ONLY the requested placeholders.

{cl_strategy_text}

{jd_strategy_text}

{evidence_text}

{CommonPrompt.source_of_truth(knowledge)}

{CommonPrompt.career_profile(knowledge)}

{CommonPrompt.career_evidence(knowledge)}

{CommonPrompt.career_library()}

{CommonPrompt.ats_keywords(knowledge)}

{CommonPrompt.positioning_rules(knowledge)}

{CommonPrompt.cover_letter_rules(knowledge)}

{content_filter}

{anti_hallucination}

{recruiter_decision}

{recruiter_review}

==================================================
FINAL INSTRUCTIONS
==================================================

Before generating the final Cover Letter:

1. Match every important Job Description requirement with verified experience.

2. Focus on business value rather than responsibilities.

3. Demonstrate why the candidate is a strong fit.

4. Expand only the strongest evidence.

5. Remove generic statements.

6. Remove repeated content.

7. Keep the letter concise and executive.

8. Strengthen recruiter confidence.

9. Maximize interview probability.

10. Produce ONLY the FINAL READY TO APPLY version.

==================================================
JOB DESCRIPTION
==================================================

{JobDescription.build(job)}

==================================================
OUTPUT FORMAT
==================================================

{OutputFormat.cl()}
""".strip()