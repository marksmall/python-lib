import ast

from plugins.bare_except import BareExceptChecker


def test_bare_except_detected() -> None:
    code = "try:\n    pass\nexcept:\n    pass"
    tree = ast.parse(code)
    checker = BareExceptChecker(tree, filename="test_bare_except.py")
    errors = list(checker.run())
    assert any("BEX100" in msg for _, _, msg, _ in errors)


def test_no_bare_except() -> None:
    code = "try:\n    pass\nexcept Exception:\n    pass"
    tree = ast.parse(code)
    checker = BareExceptChecker(tree, filename="test_bare_except.py")
    assert not list(checker.run())
