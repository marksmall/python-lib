import ast


class NewlineAfterBlockChecker:
    name = "flake8-newline-after-block"
    version = "0.1.0"

    def __init__(self, tree: ast.AST, filename: str) -> None:
        self.tree = tree
        self.filename = filename

    def run(self):
        # type: ignore[no-untyped-def]
        with open(self.filename, "r") as f:
            lines = f.readlines()
        for node in ast.walk(self.tree):
            if isinstance(node, (ast.If, ast.For, ast.While, ast.With, ast.Try)):
                end_lineno = getattr(node.body[-1], "end_lineno", node.body[-1].lineno)
                if end_lineno < len(lines):
                    next_line = lines[end_lineno].strip()
                    if next_line != "":
                        yield (
                            end_lineno + 1,
                            0,
                            "NLB100: Missing blank line after block statement.",
                            type(self),
                        )
                elif end_lineno == len(lines) and (len(lines) == 0 or not lines[-1].endswith("\n")):
                    # Block ends at last line, and last line is not blank (does not end with a newline)
                    yield (
                        end_lineno,
                        0,
                        "NLB100: Missing blank line after block statement at end of file.",
                        type(self),
                    )
