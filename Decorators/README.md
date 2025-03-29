# Decorators Exercises
# This directory contains a series of exercises to explore Python decorators.
# We will cover 15 exercises: 5 simple, 5 intermediate, and 5 advanced.
# Each exercise builds on previous topics like file handling, CSV/JSON processing,
# and function manipulation, while introducing decorator concepts to enhance functionality.

### Exercise 1: Log Call Decorator (Simple)

Write a decorator named `log_call` that:
1. Logs the function name and its arguments to a text file named "function_logs.txt" each time the function is called.
2. Executes the original function without modification.
3. Use this decorator on a simple function named `add_numbers` that takes two numbers and returns their sum.

**File Name**: `01_log_call_decorator.py`

**Sample Input:**
```python
add_numbers(3, 5)
add_numbers(10, 20)

---

