"""
modules/report/retry_prompt.py

AIJobAssistant
Version : v1.0.0
"""


class RetryPrompt:

    @staticmethod
    def build(
        original_prompt: str,
        error: Exception,
    ) -> str:

        return (
            original_prompt
            + "\n\n"
            + "==================================================\n"
            + "PREVIOUS RESPONSE FAILED VALIDATION\n"
            + "==================================================\n"
            + f"Validation Error: {error}\n\n"
            + "Regenerate the ENTIRE response.\n"
            + "Fix every validation error.\n"
            + "Do not explain anything.\n"
            + "Output ONLY the required format.\n"
        )