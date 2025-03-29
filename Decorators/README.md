# Decorators Exercises
This directory contains a series of exercises to explore Python decorators.
We will cover 15 exercises: 5 simple, 5 intermediate, and 5 advanced.
Each exercise builds on previous topics like file handling, CSV/JSON processing,
and function manipulation, while introducing decorator concepts to enhance functionality.

---


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
```

**Sample Output:**

- in the terminal:
```
8
30
```
- In "function_logs.txt":
```
Function add_numbers called with args: (3, 5)
Function add_numbers called with args: (10, 20)
```

---

### Exercise 2: Count Calls Decorator (Simple)

Write a decorator named `count_calls` that:
1. Counts the number of times the function is called and stores it in a text file named "call_counts.txt".
2. Executes the original function without modification.
3. Use this decorator on a function named `say_hello` that takes a name and prints a greeting message.

**Note**: Each time the program runs, "call_counts.txt" shows the total number of calls for that execution (it resets unless the file is manually deleted).

**File Name**: `02_count_calls_decorator.py`

**Sample Input:**
```python
say_hello("Ali")
say_hello("Sara")
say_hello("Reza")
```

**Sample Output:**
- in terminal:
```
Hello Ali!
Hello Sara!
Hello Reza!
```
- in "call_counts.txt":
```
Function say_hello has been called 3 times
```

