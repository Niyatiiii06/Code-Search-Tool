import os
import ast
IGNORED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules"
}

def find_calls(tree, function_name):
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            current_function = node.name

            for child in ast.walk(node):
                if isinstance(child, ast.Call):
                    if isinstance(child.func, ast.Name):
                        if child.func.id == function_name:

                            calls.append({
                                "caller": current_function,
                                "line": child.lineno
                            })

    return calls

def search_code(project_path, function_name):
    results = {
        "definitions": [],
        "calls": [],
        "imports": [],
        "called_by": []
    }

    for root, dirs, files in os.walk(project_path):

        dirs[:] = [
            directory
            for directory in dirs
            if directory not in IGNORED_DIRS
        ]

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

            # Find which functions call our target function
            calls = find_calls(tree, function_name)
            for call in calls:
                results["called_by"].append({
                    "file": filepath,
                    "line": call["line"],
                    "caller": call["caller"]
                })

            # Analyze AST
            for node in ast.walk(tree):
                # Function definition
                if isinstance(node, ast.FunctionDef):
                    if node.name == function_name:
                        results["definitions"].append({
                            "file": filepath,
                            "line": node.lineno,
                            "code": f"def {node.name}"
                        })

                # Function call
                elif isinstance(node, ast.Call):
                    # search_web()
                    if isinstance(node.func, ast.Name):
                        if node.func.id == function_name:
                            results["calls"].append({
                                "file": filepath,
                                "line": node.lineno,
                                "code": f"{node.func.id}()"
                            })

                    # utils.search_web()
                    elif isinstance(node.func, ast.Attribute):
                        if node.func.attr == function_name:
                            results["calls"].append({
                                "file": filepath,
                                "line": node.lineno,
                                "code": f"{node.func.value.id}.{node.func.attr}()"
                            })

                # import search_web
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name == function_name:
                            results["imports"].append({
                                "file": filepath,
                                "line": node.lineno,
                                "code": f"import {alias.name}"
                            })

                # from utils import search_web
                elif isinstance(node, ast.ImportFrom):
                    for alias in node.names:
                        if alias.name == function_name:
                            results["imports"].append({
                                "file": filepath,
                                "line": node.lineno,
                                "code": f"from {node.module} import {alias.name}"
                            })

    return results

project_path = input("Enter project path: ")
function_name = input("Enter function name: ")
results = search_code(project_path, function_name)

print("\n--- DEFINITIONS ---")
for result in results["definitions"]:
    print(
        f"{result['file']}:{result['line']} "
        f"→ {result['code']}"
    )

print("\n--- CALLS ---")
for result in results["calls"]:
    print(
        f"{result['file']}:{result['line']} "
        f"→ {result['code']}"
    )


print("\n--- IMPORTS ---")
for result in results["imports"]:
    print(
        f"{result['file']}:{result['line']} "
        f"→ {result['code']}"
    )

print("\n--- CALLED BY ---")
for result in results["called_by"]:
    print(
        f"{result['file']}:{result['line']} "
        f"→ {result['caller']}()"
    )