import ast


class NoneComparisonChecker:
    name = "flake8-none-comparison"
    version = "0.1.0"

    def __init__(self, tree: ast.AST, filename: str) -> None:
        self.tree = tree
        self.filename = filename

    def run(self):
        # type: ignore[no-untyped-def]
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Compare):
                for op, comparator in zip(node.ops, node.comparators):
                    if isinstance(comparator, ast.Constant) and comparator.value is None:
                        if isinstance(op, ast.Eq):
                            yield (
                                node.lineno,
                                node.col_offset,
                                "NCP100: Use 'is None' instead of '== None'",
                                type(self),
                            )
                        elif isinstance(op, ast.NotEq):
                            yield (
                                node.lineno,
                                node.col_offset,
                                "NCP101: Use 'is not None' instead of '!= None'",
                                type(self),
                            )
