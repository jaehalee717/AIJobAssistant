"""
modules/knowledge_loader.py

AIJobAssistant
Version : v5.0.0
"""

from pathlib import Path

from docx import Document


class KnowledgeLoader:

    KNOWLEDGE_ORDER = [
        "source_of_truth",
        "career_profile",
        "career_evidence",
        "ats_keywords",
        "interview_library",
        "positioning_rules",
        "cv_rules",
        "cover_letter_rules",
        "apply_skip_rules",
        "quality_checklist",
        "analysis_rules",
    ]

    def __init__(
        self,
        knowledge_dir: Path,
    ):

        self.knowledge_dir = knowledge_dir
        self.documents = {}

    def load(
        self,
    ) -> None:

        self.documents.clear()

        for name in self.KNOWLEDGE_ORDER:

            file = self.knowledge_dir / f"{name}.docx"

            if not file.exists():
                continue

            self.documents[name] = self._read_docx(
                file,
            )

    @staticmethod
    def _read_docx(
        file: Path,
    ) -> str:

        document = Document(
            file,
        )

        lines = []

        for paragraph in document.paragraphs:

            text = paragraph.text.strip()

            if text:

                lines.append(
                    text,
                )

        return "\n".join(
            lines,
        )

    def get(
        self,
        name: str,
    ) -> str:

        return self.documents.get(
            name,
            "",
        )

    def get_many(
        self,
        *names: str,
    ) -> str:

        return "\n\n".join(
            self.documents.get(
                name,
                "",
            )
            for name in names
            if self.documents.get(
                name,
                "",
            )
        )