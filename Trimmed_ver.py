import os
import ast

IGNORED_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules"}


def search_code(project_path, function_name):
    results = {"definitions": [], "calls": [], "imports": []}

    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]

        for file in files:
            if not file.endswith(".py"):
                continue

            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                code = f.read()

            try:
                tree = ast.parse(code)
            except SyntaxError:
                continue

            # ONE walk over the tree, checking each node once
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == function_name:
                    results["definitions"].append({
                        "file": filepath,
                        "line": node.lineno,
                        "code": f"def {node.name}"
                    })

                elif isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name) and node.func.id == function_name:
                        results["calls"].append({
                            "file": filepath,
                            "line": node.lineno,
                            "code": f"{node.func.id}()"
                        })
                    elif isinstance(node.func, ast.Attribute) and node.func.attr == function_name:
                        results["calls"].append({
                            "file": filepath,
                            "line": node.lineno,
                            "code": f"{ast.dump(node.func.value)}.{node.func.attr}()"
                        })

                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name == function_name:
                            results["imports"].append({
                                "file": filepath,
                                "line": node.lineno,
                                "code": f"import {alias.name}"
                            })

                elif isinstance(node, ast.ImportFrom):
                    for alias in node.names:
                        if alias.name == function_name:
                            results["imports"].append({
                                "file": filepath,
                                "line": node.lineno,
                                "code": f"from {node.module} import {alias.name}"
                            })

    return results