import ast

from plugins.none_comparison import NoneComparisonChecker


def test_none_comparison_detected() -> None:
    code = "if x == None:\n    pass"
    tree = ast.parse(code)
    checker = NoneComparisonChecker(tree, filename="test.py")
    errors = list(checker.run())
    assert any("NCP100" in msg for _, _, msg, _ in errors)


def test_no_none_comparison() -> None:
    code = "if x is None:\n    pass"
    tree = ast.parse(code)
    checker = NoneComparisonChecker(tree, filename="test.py")
    assert not list(checker.run())
