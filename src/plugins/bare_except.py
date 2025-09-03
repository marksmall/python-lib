import ast


class BareExceptChecker:
    name = "flake8-bare-except"
    version = "0.1.0"

    def __init__(self, tree: ast.AST, filename: str) -> None:
        self.tree = tree
        self.filename = filename

    def run(self):
        # type: ignore[no-untyped-def]
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ExceptHandler) and node.type is None:
                yield (
                    node.lineno,
                    node.col_offset,
                    "BEX100: Avoid bare except; use 'except Exception' instead.",
                    type(self),
                )
