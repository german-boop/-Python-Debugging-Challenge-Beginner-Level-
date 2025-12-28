"""
test.py
========

## Unit tests for `average.py` module.

This module provides a comprehensive test suite for the `calculate_average`
function. It ensures correctness, robustness, and consistent behavior
for various types of input, following Python best practices, PEP8 standards,
and ISO/IEC 25010 principles (functional correctness, reliability, and robustness).

Author: Your Name
Date: 2025-12-28
"""

```python

import unittest
from average import calculate_average


class TestCalculateAverage(unittest.TestCase):
    """
    Test suite for the calculate_average function.

    Each test case validates a specific scenario to ensure the function
    behaves correctly under normal, edge, and boundary conditions.
    """

    def test_normal_numbers(self):
        """Test a list of normal positive integers."""
        numbers = [1, 2, 3, 4]
        expected = 2.5
        result = calculate_average(numbers)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_empty_list(self):
        """Test an empty list input; should return 0."""
        numbers = []
        expected = 0
        result = calculate_average(numbers)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_single_value(self):
        """Test a list containing a single number; average should equal that number."""
        numbers = [10]
        expected = 10
        result = calculate_average(numbers)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_negative_numbers(self):
        """Test a list containing negative numbers."""
        numbers = [-1, -2, -3]
        expected = -2
        result = calculate_average(numbers)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_float_numbers(self):
        """Test a list of float numbers with decimal precision."""
        numbers = [1.5, 2.5, 3.5]
        expected = 2.5
        result = calculate_average(numbers)
        self.assertAlmostEqual(result, expected, places=7,
                               msg=f"Expected {expected}, got {result}")

    def test_iterable_tuple(self):
        """Test a tuple as input instead of a list."""
        numbers = (10, 20, 30)
        expected = 20
        result = calculate_average(numbers)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_large_numbers(self):
        """Test a list with very large numbers to check for numeric stability."""
        numbers = [1e10, 2e10, 3e10]
        expected = 2e10
        result = calculate_average(numbers)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_mixed_numbers(self):
        """Test a list containing both positive and negative numbers."""
        numbers = [-10, 0, 10]
        expected = 0
        result = calculate_average(numbers)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")


if __name__ == "__main__":
    # Run all tests in verbose mode for better readability
    unittest.main(verbosity=2)
```
