import ast


class NoPrintChecker:
    name = "flake8-no-print"
    version = "0.1.0"

    def __init__(self, tree: ast.AST, filename: str) -> None:
        self.tree = tree
        self.filename = filename

    def run(self):
        # type: ignore[no-untyped-def]
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "print":
                yield (
                    node.lineno,
                    node.col_offset,
                    "NP100: Avoid print statements outside test/debug code.",
                    type(self),
                )
