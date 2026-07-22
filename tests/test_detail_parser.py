"""
tests/test_detail_parser.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT),
)

from modules.detail_parser import DetailParser


def test_detail_parser_apply():

    parser = DetailParser()

    response = """
# Detail Analysis

Recommendation: APPLY

Good technical fit.
"""

    result = parser.parse(response)

    assert result.apply is True
    assert "Recommendation" in result.content


def test_detail_parser_skip():

    parser = DetailParser()

    response = """
Recommendation: SKIP
"""

    result = parser.parse(response)

    assert result.apply is False