import os
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
                    lines = f.readlines()
                for line_no, line in enumerate(lines, start=1):

                    if f"def {function_name}(" in line:

                        results.append({
                            "type": "DEFINITION",
                            "file": filepath,
                            "line": line_no,
                            "code": line.strip()
                        })

                    elif f"import {function_name}" in line:

                        results.append({
                            "type": "IMPORT",
                            "file": filepath,
                            "line": line_no,
                            "code": line.strip()
                        })

                    elif f"{function_name}(" in line:

                        results.append({
                            "type": "CALL",
                            "file": filepath,
                            "line": line_no,
                            "code": line.strip()
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