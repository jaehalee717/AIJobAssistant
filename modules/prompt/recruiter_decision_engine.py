"""
modules/prompt/recruiter_decision_engine.py

AIJobAssistant
Version : v1.0.0
"""


class RecruiterDecisionEngine:

    @staticmethod
    def instructions() -> str:

        return """
==================================================
RECRUITER DECISION ENGINE
==================================================

Think exactly like an experienced hiring manager.

The recruiter will typically evaluate the candidate in this order.

1. Can this person do the job?

2. Has this person solved similar business problems?

3. Is the experience directly relevant?

4. Does the candidate reduce hiring risk?

5. Can this person lead people, vendors and stakeholders?

6. Will this candidate fit our environment?

7. Is the CV easy to scan in 20–30 seconds?

8. Are the strongest achievements immediately visible?

9. Does every bullet create business value?

10. Would I invite this candidate for an interview?

If the answer to Question 10 is not YES:

Rewrite the CV before producing the final output.

Always optimize for interview probability.

==================================================
"""