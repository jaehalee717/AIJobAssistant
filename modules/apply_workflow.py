"""
modules/apply_workflow.py
AIJobAssistant
Version : v2.0
"""

from modules.console import console


class ApplyWorkflow:

    def __init__(
        self,
        repository,
        prompt_builder,
        ai_generator,
        parser,
        apply_service,
    ):
        self.repository = repository
        self.prompt_builder = prompt_builder
        self.ai_generator = ai_generator
        self.parser = parser
        self.apply_service = apply_service

    def run(self) -> None:

        jobs = self.repository.get_ready_to_apply()

        total = len(jobs)

        if total == 0:
            console.warning("No jobs.")
            return

        for current, job in enumerate(jobs, start=1):
            self._process_job(
                job,
                current,
                total,
            )

    def _process_job(
        self,
        job,
        current: int,
        total: int,
    ) -> None:

        self._show_screen(
            job,
            current,
            total,
        )

        prompt = self.prompt_builder.build_detail_analysis_prompt(
            job,
        )

        self.ai_generator.send(
            prompt,
        )

        console.action(
            "ChatGPT(Ctrl+V → 응답복사) | AIJobAssistant(Ctrl+V → ENTER)"
        )

        self._wait_for_user()

        response = self.ai_generator.read_response()

        result = self.parser.parse(
            response,
        )

        self.repository.save_detail_result(
            job.id,
            result,
        )

        if result.apply:

            self.apply_service.run(
                job,
            )

            self.repository.mark_ready_for_apply(
                job.id,
            )
        else:

            self.repository.mark_skipped(
                job.id,
            )

    def _show_screen(
        self,
        job,
        current: int,
        total: int,
    ) -> None:

        console.clear()

        console.header(
            step="2/6",
            title="Detail Analysis",
            current=current,
            total=total,
        )

        console.job(
            job,
        )

        console.progress(
            current=current,
            total=total,
        )

    def _wait_for_user(self) -> None:
      input()