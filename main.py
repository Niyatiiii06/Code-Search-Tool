from code_search import search_code


project_path = input("Enter project path: ")
function_name = input("Enter function name: ")

results = search_code(
    project_path,
    function_name
)


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