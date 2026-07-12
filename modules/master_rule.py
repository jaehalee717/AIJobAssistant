"""
master_rule.py
v0.8

Apply Job Recommendation Rules
"""

from typing import Dict


class MasterRule:

    def evaluate(self, job: Dict) -> Dict:

        score = 50
        reasons = []

        position = job.get("position", "").lower()
        description = job.get("description", "").lower()
        location = job.get("location", "").lower()

        keywords = [
            "it manager",
            "head of it",
            "it director",
            "information security",
            "cyber security",
            "cybersecurity",
            "governance",
            "grc",
            "infrastructure",
            "service delivery",
            "it operations",
            "digital transformation",
            "project manager"
        ]

        for keyword in keywords:
            if keyword in position or keyword in description:
                score += 5
                reasons.append(keyword)

        if "spain" in location:
            score += 10

        if "remote" in location:
            score += 5

        score = min(score, 100)

        if score >= 80:
            decision = "RECOMMEND"
        elif score >= 60:
            decision = "REVIEW"
        else:
            decision = "SKIP"

        return {
            "score": score,
            "decision": decision,
            "reason": ", ".join(reasons) if reasons else "General evaluation"
        }