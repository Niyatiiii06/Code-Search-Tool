import ast


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


code = """
def research():
    search_web("AI")

def summarize():
    search_web("machine learning")

def main():
    research()
"""

tree = ast.parse(code)

calls = find_calls(tree, "search_web")

print(calls)