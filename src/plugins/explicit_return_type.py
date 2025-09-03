import ast


class ExplicitReturnTypeChecker:
    name = "flake8-explicit-return-type"
    version = "0.1.0"

    def __init__(self, tree: ast.AST, filename: str) -> None:
        self.tree = tree
        self.filename = filename

    def run(self):
        # type: ignore[no-untyped-def]
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef) and node.returns is None:
                yield (
                    node.lineno,
                    node.col_offset,
                    "ERT100: Function missing explicit return type annotation.",
                    type(self),
                )
