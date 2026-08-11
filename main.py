import os
import ast
IGNORED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules"
}

def search_code(project_path, function_name):
    results = []

    for root, dirs, files in os.walk(project_path):

        dirs[:] = [
            directory
            for directory in dirs
            if directory not in IGNORED_DIRS
        ]

        for file in files:

            if file.endswith(".py"):

                filepath = os.path.join(root, file)

                with open(filepath, "r", encoding="utf-8") as f:
                    code = f.read()

                tree = ast.parse(code)

                for node in ast.walk(tree):

                    if isinstance(node, ast.FunctionDef):

                        if node.name == function_name:

                            results.append({
                                "type": "DEFINITION",
                                "file": filepath,
                                "line": node.lineno,
                                "code": f"def {node.name}"
                            })
                    elif isinstance(node, ast.Call):

                        if isinstance(node.func, ast.Name):

                            if node.func.id == function_name:

                                results.append({
                                    "type": "CALL",
                                    "file": filepath,
                                    "line": node.lineno,
                                    "code": f"{node.func.id}()"
                                })

    return results

project_path = input("Enter project path: ")
function_name = input("Enter function name: ")
results = search_code(project_path, function_name)

for result in results:
    print(
        f"{result['type']} → "
        f"{result['file']}:{result['line']} "
        f"→ {result['code']}"
    )