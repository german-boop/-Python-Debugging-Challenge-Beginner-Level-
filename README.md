# 🐍 Python Debugging Challenge (Beginner Level)

## 📖 Overview

This repository contains a **beginner-level Python debugging challenge** designed according to:

- **International programming standards**
- **ISO/IEC 25010 software quality principles**
- **PEP 8 & PEP 484 Python best practices**

The goal is to help programmers improve their ability to **identify bugs, fix logic errors, and write clean, maintainable code**.

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

## ❌ Buggy Code

```python
def average(numbers):
    total = 0
    for n in numbers
        total += n
    return total

Note: The above code contains syntax and logic errors.
