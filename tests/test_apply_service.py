"""
tests/test_apply_service.py
AIJobAssistant
Version : v2.0.0
"""

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