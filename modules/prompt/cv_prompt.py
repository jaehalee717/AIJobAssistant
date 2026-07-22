"""
modules/prompt/cv_prompt.py

AIJobAssistant
Version : v3.2.0
"""

from .anti_hallucination import AntiHallucination
from .common_prompt import CommonPrompt
from .content_filter import ContentFilter
from .cv_strategy import CVStrategy
from .evidence_strategy import EvidenceStrategy
from .jd_strategy import JDStrategy
from .job_description import JobDescription
from .output_format import OutputFormat
from .recruiter_decision_engine import RecruiterDecisionEngine
from .recruiter_review import RecruiterReview


class CVPrompt:

    @staticmethod
    def build(
        job,
        knowledge,
    ) -> str:

        cv_strategy = CVStrategy.build(
            job,
        )

        cv_strategy_text = CVStrategy.to_text(
            cv_strategy,
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
You are an expert Executive Resume Writer specializing in ATS-optimized executive resumes.

Your objective is NOT simply to write a CV.

Your objective is to maximize:

• Interview Probability
• Recruiter Confidence
• ATS Compatibility
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
- Use ATS keywords naturally.
- Do NOT copy the Job Description.
- Do NOT use Markdown.
- Do NOT explain your reasoning.
- Output ONLY the requested placeholders.

{cv_strategy_text}

{jd_strategy_text}

{evidence_text}

{CommonPrompt.source_of_truth(knowledge)}

{CommonPrompt.career_profile(knowledge)}

{CommonPrompt.career_evidence(knowledge)}

{CommonPrompt.career_library()}

{CommonPrompt.ats_keywords(knowledge)}

{CommonPrompt.positioning_rules(knowledge)}

{CommonPrompt.cv_rules(knowledge)}

{content_filter}

{anti_hallucination}

{recruiter_decision}

{recruiter_review}

==================================================
FINAL INSTRUCTIONS
==================================================

Before generating the final CV:

1. Select the strongest realistic positioning.

2. Match every important Job Description requirement with verified experience.

3. Prioritize the most relevant experience.

4. Expand only the strongest evidence.

5. Compress low-value experience.

6. Remove duplicated business value.

7. Remove repeated ATS keywords.

8. Remove weak, generic or low-value bullets.

9. Strengthen recruiter confidence.

10. Keep the CV within two pages.

11. Optimize for interview probability.

12. Produce ONLY the FINAL READY TO APPLY version.

==================================================
JOB DESCRIPTION
==================================================

{JobDescription.build(job)}

==================================================
OUTPUT FORMAT
==================================================

{OutputFormat.cv()}
""".strip()