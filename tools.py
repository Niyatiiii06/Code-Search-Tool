from langchain_core.tools import tool

from code_search import search_code


@tool
def code_search_tool(project_path: str, function_name: str) -> dict:
    """
    Search a Python project for a function or method.

    Finds:
    - definitions
    - calls
    - imports
    - functions that call the target
    """

    return search_code(
        project_path,
        function_name
    )