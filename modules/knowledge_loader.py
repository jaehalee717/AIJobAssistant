"""
modules/knowledge_loader.py
AIJobAssistant
Version : v1.5.0
"""

from __future__ import annotations

from pathlib import Path

from docx import Document


class KnowledgeLoader:
    """Knowledge Loader"""

    def __init__(self, knowledge_dir: Path):

        self.knowledge_dir = Path(knowledge_dir)
        self.knowledge = {}

    def load(self) -> dict[str, str]:
        """
        Load all knowledge files into memory.
        """

        self.knowledge.clear()

        for file in sorted(self.knowledge_dir.glob("*.docx")):

            self.knowledge[file.stem] = self._read_docx(file)

        return self.knowledge

    def get(
        self,
        name: str,
    ) -> str:

        return self.knowledge.get(name, "")

    def get_many(
        self,
        names: list[str],
    ) -> str:
        """
        Load only selected knowledge documents.
        """

        texts = []

        for name in names:

            text = self.get(name)

            if not text:
                continue

            texts.append(f"===== {name} =====")
            texts.append(text)
            texts.append("")

        return "\n".join(texts)

    def get_all(self) -> str:

        texts = []

        for name, text in self.knowledge.items():

            texts.append(f"===== {name} =====")
            texts.append(text)
            texts.append("")

        return "\n".join(texts)

    @staticmethod
    def _read_docx(path: Path) -> str:

        document = Document(path)

        lines = []

        for paragraph in document.paragraphs:

            text = paragraph.text.strip()

            if text:
                lines.append(text)

        return "\n".join(lines)