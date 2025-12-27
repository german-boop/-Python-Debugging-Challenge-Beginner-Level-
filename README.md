# 🐍 Python Debugging Challenge (Beginner Level)

## 📖 Overview

This repository contains a **beginner-level Python debugging challenge** designed according to:

- **International programming standards**
- **ISO/IEC 25010 software quality principles**
- **PEP 8 & PEP 484 Python best practices**

The goal is to help programmers improve their ability to **identify bugs, fix logic errors, and write clean, maintainable code**.

## 📁 Suggested Repository Structure (with Tests)

```plaintext
python-debugging-challenge/
│
├── average.py
├── tests/
│   └── test_average.py
├── README.md
└── LICENSE

---

## 🎯 Learning Objectives

After completing this challenge, you will be able to:

- Detect and fix at least 3 types of Python bugs (syntax, logic, runtime)
- Write readable and maintainable Python code
- Follow **PEP 8** and **PEP 484** standards
- Ensure your code passes unit tests
- Improve software quality according to **ISO/IEC 25010**

---

## 🧩 Challenge Description

You are given a Python function intended to calculate the **average of a list of numbers**.  

The original version contains:

- A syntax error
- A logic error
- No handling for empty input

Your task is to modify the function so that it functions correctly and adheres to best practices.

### Example

| Input        | Output |
|-------------|--------|
| `[2, 4, 6]` | `4.0`  |
| `[]`        | `0.0`  |

---

## 📝 Examples

```python
# Example 1
Input: [2, 4, 6]
Output: 4.0

# Example 2
Input: []
Output: 0.0

## 🐞 Example of a Buggy Function

```python
# This function is intended to calculate the average of a list
# Bug: Syntax error and logic error

def average(numbers):
    total = 0
    for n in numbers:  # <- missing colon was added
        total += n
    return total  # <- logic error: should divide by len(numbers)

Note: The above code contains syntax and logic errors.

## ✅ Correct Solution

```python
from typing import List

def calculate_average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (List[float]): A list of numeric values.

    Returns:
        float: The average value. Returns 0.0 if the list is empty.
    """
    if not numbers:
        return 0.0

    total = sum(numbers)
    return total / len(numbers)

## 📌 Requirements

- Python 3.10+
- No external libraries
- Works on Windows, Linux, and MacOS


## Evaluation Criteria

| Criterion    | Description                          |
|--------------|--------------------------------------|
| Correctness  | Returns the correct average          |
| Robustness   | Handles empty lists safely           |
| Readability  | Clear structure and naming           |
| Standards    | Follows PEP 8 and PEP 484            |


## ✅ Detailed Evaluation Criteria

- **Correctness:** Function passes all unit tests
- **Robustness:** Handles empty and invalid input without crashing
- **Readability:** PEP8 linting score > 8/10
- **Standards:** Type hints and docstring included

## ✅ References

- **PEP 8 – Style Guide for Python Code**, Python Software Foundation, 2025. Available at: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/) [Accessed: Dec 27, 2025]

## ⚖️ License

This project is released for educational purposes and follows an **MIT License**.


