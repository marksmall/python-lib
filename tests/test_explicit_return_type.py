import ast

from plugins.explicit_return_type import ExplicitReturnTypeChecker


def test_explicit_return_type_missing() -> None:
    code = "def foo():\n    return 1"
    tree = ast.parse(code)
    checker = ExplicitReturnTypeChecker(tree, filename="test_explicit_return_type.py")
    errors = list(checker.run())
    assert any("ERT100" in msg for _, _, msg, _ in errors)


def test_explicit_return_type_present() -> None:
    code = "def foo() -> int:\n    return 1"
    tree = ast.parse(code)
    checker = ExplicitReturnTypeChecker(tree, filename="test_explicit_return_type.py")
    assert not list(checker.run())
