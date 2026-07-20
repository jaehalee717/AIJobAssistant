"""
modules/apply_service.py
AIJobAssistant
Version : v1.5.0
"""

from pathlib import Path
import tkinter as tk

from config import PROJECT_ROOT

from models.job import Job

from database.sqlite_manager import SQLiteManager

from modules.ai_generator import AIGenerator
from modules.cl_generator import CLGenerator
from modules.cv_generator import CVGenerator
from modules.knowledge_loader import KnowledgeLoader
from modules.output_manager import OutputManager
from modules.pdf_converter import PDFConverter
from modules.prompt_builder import PromptBuilder


class ApplyService:

    def __init__(self):

        self.knowledge = KnowledgeLoader(
            PROJECT_ROOT / "knowledge"
        )

        self.knowledge.load()

        self.prompt_builder = PromptBuilder(
            self.knowledge
        )

        self.ai = AIGenerator()

        self.cv_generator = CVGenerator(
            PROJECT_ROOT / "templates" / "Jaeha_Lee_CV.docx"
        )

        self.cl_generator = CLGenerator(
            PROJECT_ROOT / "templates" / "Jaeha_Lee_CL.docx"
        )

    def run(self):

        print("=" * 80)
        print("AIJobAssistant v1.5.0")
        print("Apply")
        print("=" * 80)

        job = self.load_ready_job()

        output = OutputManager(job)

        cv_prompt = self.prompt_builder.build_cv_prompt(job)

        self.ai.generate_cv(cv_prompt)

        cv_text = self.wait_for_ai(
            "CV Prompt copied to Clipboard."
        )

        cl_prompt = self.prompt_builder.build_cl_prompt(job)

        self.ai.generate_cl(cl_prompt)

        cl_text = self.wait_for_ai(
            "Cover Letter Prompt copied to Clipboard."
        )

        cv_docx = output.get_cv_docx_path()

        cl_docx = output.get_cl_docx_path()

        self.cv_generator.generate(
            output_path=cv_docx,
            profile=cv_text,
            competencies="",
            tai="",
            brazil="",
            spain="",
        )

        self.cl_generator.generate(
            output_path=cl_docx,
            letter=cl_text,
        )

        pdf = PDFConverter()

        pdf.convert(
            cv_docx,
            output.get_cv_pdf_path(),
        )

        pdf.convert(
            cl_docx,
            output.get_cl_pdf_path(),
        )

        pdf.close()

        output.save_job_description(
            job.description
        )

        output.save_salary(
            job.salary
        )

        output.save_report(job)

        if job.apply_url:
            db = SQLiteManager()
            db.update_apply_status(job.apply_url)
            db.close()

        print()
        print("=" * 80)
        print("Completed.")
        print(output.output_dir)
        print("=" * 80)

    @staticmethod
    def get_clipboard() -> str:

        print("Opening Tk...")

        root = tk.Tk()
        root.withdraw()

        print("Reading clipboard...")

        text = root.clipboard_get()

        print("Clipboard successfully read.")

        root.destroy()

        return text.strip()

    def wait_for_ai(
        self,
        message: str,
    ) -> str:

        print()
        print("=" * 80)
        print(message)
        print("Copy the ChatGPT response.")
        print("Press ENTER.")
        print("=" * 80)

        value = input()

        print(f"input() returned: {repr(value)}")
        print("Reading clipboard...")

        text = self.get_clipboard()

        print(f"Clipboard length: {len(text)}")
        print("Clipboard read completed.")

        return text

    @staticmethod
    def load_ready_job() -> Job:
        """
        Load next READY_TO_APPLY job from SQLite.
        """

        db = SQLiteManager()

        row = db.get_ready_to_apply_job()

        db.close()

        if row is None:
            raise RuntimeError(
                "No READY_TO_APPLY job found."
            )

        job = Job()

        job.company = row.get("company", "")
        job.position = row.get("position", "")
        job.country = row.get("country", "")
        job.city = row.get("city", "")

        if job.city:
            job.location = f"{job.city}, {job.country}"
        else:
            job.location = job.country

        job.salary = row.get("salary", "")
        job.apply_url = row.get("url", "")

        job.description = row.get("description", "")

        return job