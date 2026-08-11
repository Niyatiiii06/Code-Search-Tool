import os


def search_code(project_path, function_name):
    results = []
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                for line_no, line in enumerate(lines, start=1):

                    if f"def {function_name}" in line:
                        results.append(
                            f"DEFINITION → {filepath}:{line_no}"
                        )

                    elif f"import {function_name}" in line:
                        results.append(
                            f"IMPORT → {filepath}:{line_no}"
                        )

                    elif f"{function_name}(" in line:
                        results.append(
                            f"CALL → {filepath}:{line_no}"
                        )
    return results


project_path = "sample_project"
function_name = input("Enter function name: ")
results = search_code(project_path, function_name)

for result in results:
    print(result)