"""
tests/test_apply_service.py
AIJobAssistant
Version : v2.0.0
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT),
)

from modules.apply_service import ApplyService


def test_apply_service_initialize():

    service = ApplyService()

    assert service.knowledge is not None
    assert service.prompt_builder is not None
    assert service.ai is not None

    assert service.cv_generator is not None
    assert service.cl_generator is not None

    assert service.cv_service is not None
    assert service.cl_service is not None