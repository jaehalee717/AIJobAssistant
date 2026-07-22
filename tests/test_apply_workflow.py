"""
tests/test_apply_workflow.py
"""

from unittest.mock import Mock

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT),
)

from modules.apply_workflow import ApplyWorkflow

class DummyJob:
    id = 1
    company = "Microsoft"
    position = "Senior IT Infrastructure Manager"
    location = "Madrid"
    salary = "€70K"

class DummyResult:
    apply = True

def test_apply_workflow():

    job = DummyJob()

    repository = Mock()
    repository.get_ready_to_apply.return_value = [job]
    repository.save_detail_result = Mock()
    repository.mark_ready_for_apply = Mock()
    repository.mark_skipped = Mock()

    prompt_builder = Mock()
    prompt_builder.build_detail_analysis_prompt.return_value = "PROMPT"

    ai = Mock()
    ai.send = Mock()
    ai.read_response.return_value = "RESULT"

    parser = Mock()
    parser.parse.return_value = DummyResult()

    apply_service = Mock()

    workflow = ApplyWorkflow(
        repository=repository,
        prompt_builder=prompt_builder,
        ai_generator=ai,
        parser=parser,
        apply_service=apply_service,
    )

    workflow._wait_for_user = Mock()

    workflow._process_job(
        job,
        current=1,
        total=1,
    )

    ai.send.assert_called_once_with("PROMPT")
    ai.read_response.assert_called_once()

    parser.parse.assert_called_once_with("RESULT")

    repository.save_detail_result.assert_called_once_with(
        job.id,
        parser.parse.return_value,
    )

    repository.mark_ready_for_apply.assert_called_once_with(
        job.id,
    )

    repository.mark_skipped.assert_not_called()

    apply_service.run.assert_called_once_with(job)