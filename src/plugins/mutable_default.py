import ast


class MutableDefaultChecker:
    name = "flake8-mutable-default"
    version = "0.1.0"

    def __init__(self, tree: ast.AST, filename: str) -> None:
        self.tree = tree
        self.filename = filename

    def run(self):
        # type: ignore[no-untyped-def]
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                for default in node.args.defaults:
                    if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                        yield (
                            node.lineno,
                            node.col_offset,
                            "MD100: Avoid mutable default arguments.",
                            type(self),
                        )
