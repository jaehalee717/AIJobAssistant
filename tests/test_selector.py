from modules.selection.selector import Selector


def test_single():
    assert Selector.select(
        ["A", "B", "C"],
        "2",
    ) == ["B"]


def test_multiple():
    assert Selector.select(
        ["A", "B", "C", "D", "E"],
        "1,3,5",
    ) == ["A", "C", "E"]


def test_range():
    assert Selector.select(
        ["A", "B", "C", "D", "E"],
        "2-4",
    ) == ["B", "C", "D"]


def test_mixed():
    assert Selector.select(
        ["A", "B", "C", "D", "E", "F"],
        "1,3-5",
    ) == ["A", "C", "D", "E"]