# Code Search Tool

A lightweight Python code-search utility that analyzes a Python project using the **Abstract Syntax Tree (AST)**.

The project was built to understand how a developer tool can inspect and analyze a codebase programmatically without relying on an LLM.

---

## Features

Given a project folder and a function name, the tool searches through Python files and identifies:

- Function definitions
- Class method definitions
- Function calls
- Method calls
- Imports

The results are returned in a structured format containing the file path, line number, and matched code.

---

## Architecture

```text
Python Project
      ↓
   os.walk()
      ↓
Find Python files
      ↓
Read source code
      ↓
   ast.parse()
      ↓
CodeSearchVisitor
      ↓
AST analysis
      ↓
Definitions / Calls / Imports
      ↓
Structured Results
