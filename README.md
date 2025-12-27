
# 🐍 Python Debugging Challenge (Beginner Level)

## 📖 Overview

This repository contains a **beginner-level Python debugging challenge** designed in accordance with **international programming standards**, **ISO/IEC software quality principles**, and **Python best practices**.

The goal of this challenge is to help programmers improve their ability to **identify bugs, fix logic errors, and write clean, readable Python code**.

## 📂 Project Structure 

```text
python-debugging-challenge/
│
├── average.py
├── tests/
│   └── test_average.py
├── assets/
│   ├── average_example.png
│   └── average_demo.gif
├── README.md
├── LICENSE
└── CONTRIBUTING.md  
```
---

### 📄 File Descriptions

- `CONTRIBUTING.md`: Guidelines for contributing to this project.
- `average.py`: Contains the main Python function `calculate_average`.
- `tests/`: Unit tests for the project using `unittest`.
- `assets/`: Images and GIFs demonstrating the functionality.
- `README.md`: Full project documentation, including usage and examples.
- `LICENSE`: Open-source license (MIT recommended).

## 🎯 Learning Objectives

By completing this challenge, you will learn to:

- Detect and fix common Python bugs
- Understand basic logic and runtime errors
- Write clean and maintainable code
- Follow **PEP 8** coding standards
- Improve software quality based on **ISO/IEC 25010**

---

## 🧩 Challenge Description

You are given a Python function that is supposed to calculate the **average of a list of numbers**.

The original version of the function contains:
- A syntax error
- A logic error
- No handling for empty input

Your task is to modify the function so that it works correctly and adheres to best practices.

## 🐞 Example of a Buggy Function

```python
# This function is intended to calculate the average of a list
# Bug: Syntax error and logic error

def average(numbers):
    total = 0
    for n in numbers:  # <- missing colon was added
        total += n
    return total  # <- logic error: should divide by len(numbers)
```
## 📝 Examples

```python
# Example 1
Input: [2, 4, 6]
Output: 4.0

# Example 2
Input: []
Output: 0.0
```

## 📌 Requirements

- Python 3.10+
- No external libraries
- Works on Windows, Linux, and MacOS

## 6️⃣ Evaluation Criteria

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

- **PEP 8 – Style Guide for Python Code**, Python Software Foundation, 2025.
-  Available at    [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/) [Accessed: Dec 27, 2025]

## ⚖️ License

This project is released for educational purposes and follows an **MIT License**.


