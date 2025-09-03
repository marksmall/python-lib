import ast

from plugins.no_print import NoPrintChecker


def test_print_detected() -> None:
    code = "print('Hello')"
    tree = ast.parse(code)
    checker = NoPrintChecker(tree, filename="test_input.py")
    errors = list(checker.run())
    assert any("NP100" in error[2] for error in errors)


def test_no_print() -> None:
    code = "pass"
    tree = ast.parse(code)
    checker = NoPrintChecker(tree, filename="test_input.py")
    assert not list(checker.run())
