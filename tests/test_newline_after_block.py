import ast
import tempfile

from plugins.newline_after_block import NewlineAfterBlockChecker


def test_no_error_on_good_code() -> None:
    code = "if True:\n    pass\n"
    tree = ast.parse(code)
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp.flush()
        checker = NewlineAfterBlockChecker(tree, filename=tmp.name)
        assert not list(checker.run())


def test_error_on_missing_newline() -> None:
    code = "if True:\n    pass"  # No trailing newline to trigger missing blank line
    tree = ast.parse(code)
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp.flush()
        checker = NewlineAfterBlockChecker(tree, filename=tmp.name)
        errors = list(checker.run())
        assert any("NLB100" in msg for _, _, msg, _ in errors)
