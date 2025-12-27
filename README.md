# Python Debugging Challenge — Beginner Level

## 📁 Repository Structure (with Tests)

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

---

## 📝 Examples

### Example 1
Input: `[2, 4, 6]`  
Output: `4.0`

### Example 2
Input: `[]`  
Output: `0.0`

---

## 🐞 Example of a Buggy Function

```python
# This function is intended to calculate the average of a list
# Bug: Syntax error and logic error

def average(numbers):
    total = 0
    for n in numbers:  # <- missing colon was added
        total += n
    return total  # <- logic error: should divide by len(numbers)
