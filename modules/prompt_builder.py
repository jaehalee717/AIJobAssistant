"""
modules/prompt_builder.py

AIJobAssistant
Version : v3.0.0
"""

class PromptBuilder:

    def __init__(
        self,
        knowledge,
    ):

        self.knowledge = knowledge

    def build_cv_prompt(
        self,
        job,
    ) -> str:

        return f"""
    You are an expert Executive Resume Writer specializing in ATS-optimized executive resumes.
    Generate a customized executive CV that maximizes ATS compatibility while remaining completely truthful.

    ==================================================
    ABSOLUTE RULES
    ==================================================
    - Use ONLY verified information contained in Source of Truth and Career Library.
    - Source of Truth has the highest priority.
    - Career Library contains additional verified candidate information.
    - Never invent responsibilities, achievements, technologies, certifications, education, dates or business results.
    - Never invent or infer experience that is not explicitly supported by the Source of Truth or Career Library.
    - Tailor the wording, emphasis and ordering of verified experience to maximize relevance to the Job Description.
    - If a Job Description requirement is not supported by verified experience, do NOT mention it. Instead, emphasize the closest verified experience.
    - Preserve factual accuracy at all times.
    - Prioritize the strongest matching experience.
    - Use ATS keywords naturally.
    - Do NOT stuff keywords.
    - Always output every placeholder.
    - Output ONLY the placeholders below.
    - Do NOT use Markdown.
    - Do NOT explain your reasoning.
    - Do NOT output any text before or after the placeholders.

    ==================================================
    SOURCE OF TRUTH
    ==================================================
    {self.knowledge.get("source_of_truth")}

    ==================================================
    CAREER LIBRARY
    ==================================================
    {self.knowledge.get("career_profile")}

    ==================================================
    CAREER EVIDENCE
    ==================================================
    {self.knowledge.get("career_evidence")}

    ==================================================
    ATS KEYWORDS
    ==================================================
    {self.knowledge.get("ats_keywords")}

    ==================================================
    POSITIONING RULES
    ==================================================
    {self.knowledge.get("positioning_rules")}

    ==================================================
    CV WRITING RULES
    ==================================================
    {self.knowledge.get("cv_rules")}

    ==================================================
    JOB DESCRIPTION
    ==================================================
    {self._job_description(job)}

    ==================================================
    FINAL INSTRUCTION
    ==================================================

    This instruction overrides every previous instruction.
    Return ONLY the placeholders and their content.
    Your FIRST line MUST be:

    {{TITLE}}

    Keep every placeholder exactly as written.
    Do NOT remove or rename any placeholder.
    Do NOT output any text before {{TITLE}}.

    ==================================================
    OUTPUT FORMAT
    ==================================================
    {self._output_format("CV")}
    """.strip()

    def build_cl_prompt(
        self,
        job,
    ) -> str:

        return f"""
    You are an expert Executive Cover Letter Writer.
    Generate a customized executive cover letter that maximizes ATS compatibility while remaining completely truthful.

    ==================================================
    ABSOLUTE RULES
    ==================================================
    - Use ONLY verified information contained in Source of Truth and Career Library.
    - Source of Truth has the highest priority.
    - Career Library contains additional verified candidate information.
    - Never invent responsibilities, achievements, technologies, certifications, education, dates or business results.
    - Never infer experience that is not explicitly supported.
    - Tailor wording and emphasis to the Job Description.
    - Preserve factual accuracy.
    - Keep a professional executive tone.
    - Output ONLY the placeholders below.
    - Always output every placeholder.
    - Do NOT use Markdown.
    - Do NOT explain your reasoning.
    - Do NOT output any text before or after the placeholders.

    ==================================================
    SOURCE OF TRUTH
    ==================================================
    {self.knowledge.get("source_of_truth")}

    ==================================================
    CAREER LIBRARY
    ==================================================
    {self.knowledge.get("career_profile")}

    ==================================================
    CAREER EVIDENCE
    ==================================================
    {self.knowledge.get("career_evidence")}

    ==================================================
    ATS KEYWORDS
    ==================================================
    {self.knowledge.get("ats_keywords")}

    ==================================================
    POSITIONING RULES
    ==================================================
    {self.knowledge.get("positioning_rules")}

    ==================================================
    COVER LETTER WRITING RULES
    ==================================================
    {self.knowledge.get("cover_letter_rules")}

    ==================================================
    JOB DESCRIPTION
    ==================================================
    {self._job_description(job)}

    ==================================================
    FINAL INSTRUCTION
    ==================================================

    This instruction overrides every previous instruction.

    Return ONLY the placeholders and their content.

    Your FIRST line MUST be:

    {{GREETING}}

    Keep every placeholder exactly as written.

    Do NOT remove or rename any placeholder.

    Do NOT output any text before {{GREETING}}.

    ==================================================
    OUTPUT FORMAT
    ==================================================
    {self._output_format("CL")}
    """.strip()

    def build_analysis_prompt(
        self,
        job,
    ) -> str:

        knowledge = self.knowledge.get_many(
            "career_profile",
            "career_evidence",
            "analysis_rules",
            "apply_skip_rules",
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
        job,
    ) -> str:

        knowledge = self.knowledge.get_many(
            "career_profile",
            "career_evidence",
            "analysis_rules",
            "apply_skip_rules",
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

    @staticmethod
    def _job_description(
        job,
    ) -> str:

        return f"""
Company
{job.company}

Position
{job.position}

Location
{job.location}

Job Description
{job.description}
"""

    @staticmethod
    def _output_format(
        document_type,
    ) -> str:

        if document_type == "CV":

            return """
Return EXACTLY in the following format.

Output EVERY placeholder exactly once.

Do NOT change any placeholder name.

Do NOT remove the curly braces.

Output the placeholder first, followed by its content.

{{TITLE}}

...

{{PROFESSIONAL_PROFILE}}

...

{{CORE_COMPETENCIES}}

...

{{TAI_EXPERIENCE}}

...

{{BRAZIL_TITLE}}

...

{{BRAZIL_EXPERIENCE}}

...

{{SPAIN_EXPERIENCE}}

...

{{BANKEPOST_EXPERIENCE}}

...

{{LGI_EXPERIENCE}}

...

{{LGE_EXPERIENCE}}

...

Rules

- Every placeholder must appear exactly once.
- Keep every placeholder exactly as written.
- Output ONLY the placeholders and their content.
- Do NOT use Markdown.
- Do NOT add explanations.
- Do NOT output any text before the first placeholder.
- Do NOT output any text after the last placeholder.
"""
        return """
Return EXACTLY in the following format.

Output EVERY placeholder exactly once.

Do NOT change any placeholder name.

Do NOT remove the curly braces.

{{GREETING}}

...

{{BODY}}

...

Rules

- Every placeholder must appear exactly once.
- Keep every placeholder exactly as written.
- Output ONLY the placeholders and their content.
- Do NOT use Markdown.
- Do NOT add explanations.
- Do NOT output any text before the first placeholder.
- Do NOT output any text after the last placeholder.
"""