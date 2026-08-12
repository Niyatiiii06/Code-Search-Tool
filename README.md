##Code Search Tool

A lightweight Python code-search utility that analyzes a Python project using the Abstract Syntax Tree (AST).

The goal of this project is to understand how developer tools can inspect a codebase programmatically without relying on an LLM.

What it does

Given a project folder and a function name, the tool searches Python files and reports:

Function definitions
Function calls
Imports

It also recognizes methods defined inside classes.

Architecture
Python Project
      ↓
os.walk()
      ↓
Find .py files
      ↓
Read source code
      ↓
ast.parse()
      ↓
CodeSearchVisitor
      ↓
Definitions / Calls / Imports
      ↓
Structured Results
Example

Input:

Enter project path: sample_project
Enter function name: search_web

Example output:

--- DEFINITIONS ---
sample_project/utils.py:1 → def search_web
sample_project/client.py:3 → Client.search_web()

--- CALLS ---
sample_project/main.py:5 → search_web()
sample_project/tools.py:5 → search_web()
sample_project/main.py:18 → client.search_web()

--- IMPORTS ---
sample_project/main.py:1 → from utils import search_web
Technologies
Python
os — directory and file traversal
ast — Python Abstract Syntax Tree analysis

No LLM or vector database is required.

Project Structure
Code-Search-Tool/
│
├── main.py
├── code_search.py
├── sample_project/
│   ├── main.py
│   ├── tools.py
│   └── utils.py
│
├── README.md
└── .gitignore
How to Run

From the project directory:

python main.py

The program asks for:

Enter project path:
Enter function name:

For example:

Enter project path: sample_project
Enter function name: search_web
Key Concepts Learned
File Traversal

os.walk() recursively searches through a project directory.

AST Parsing

Python's ast module parses source code into a syntax tree, allowing the program to identify actual Python constructs rather than simply searching text.

AST Visitor

ast.NodeVisitor is used to walk through the syntax tree and detect:

FunctionDef
Call
Import
ImportFrom
Structured Results

The search function returns dictionaries containing information such as:

{
    "file": "sample_project/utils.py",
    "line": 1,
    "code": "def search_web"
}
Project Scope

This is the core v1 Code Search Tool.

The project intentionally focuses on:

File traversal
     ↓
AST analysis
     ↓
Function definitions
     ↓
Function calls
     ↓
Imports
     ↓
Structured results

Advanced features such as AI agents, LangChain tools, GitHub repository fetching, call graphs, and advanced dependency analysis are outside the scope of this version.

Learning Progression

This project is part of a larger AI engineering learning path:

PDF RAG
   ↓
YouTube RAG
   ↓
Code Search Tool
   ↓
Multi-Document RAG
   ↓
Web + RAG
   ↓
RAG + Tools
   ↓
Agents
   ↓
Multi-Agent Systems

The Code Search Tool serves as a foundation for understanding how AI systems can interact with and reason about real codebases.
