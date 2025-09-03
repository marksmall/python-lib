import ast

from plugins.mutable_default import MutableDefaultChecker


def test_mutable_default_detected() -> None:
    code = "def foo(bar=[]):\n    pass"
    tree = ast.parse(code)
    checker = MutableDefaultChecker(tree, filename="test_mutable_default.py")
    errors = list(checker.run())
    assert any("MD100" in msg for _, _, msg, _ in errors)


def test_no_mutable_default() -> None:
    code = "def foo(bar=None):\n    pass"
    tree = ast.parse(code)
    checker = MutableDefaultChecker(tree, filename="test_mutable_default.py")
    assert not list(checker.run())
