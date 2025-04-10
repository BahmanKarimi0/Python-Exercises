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

---

---

### Exercise 3: Time Execution Decorator (Simple)

Write a decorator named `time_execution` that:  
1. Measures the execution time of the function (in seconds) and writes it to a text file named "execution_times.txt".  
2. Executes the original function without modification.  
3. Use this decorator on a function named `slow_sum` that takes two numbers, includes a 1-second artificial delay (using `time.sleep`), and returns their sum.

**File Name**: `03_time_execution_decorator.py`

**Sample Input**:  
```python
slow_sum(5, 10)
slow_sum(3, 7)
```

**Sample Output**:  

- in the terminal
```
15
10
```

- In "execution_times.txt":
```
Function slow_sum took approximately 1.0 seconds
Function slow_sum took approximately 1.0 seconds
```

---

### Exercise 4: Cache Result Decorator (Simple)

Write a decorator named `cache_result` that:  
1. Stores the function's result in a text file named "function_cache.txt" (in the format "inputs:output").  
2. Returns the cached result if the function is called again with the same inputs, without re-executing the function.  
3. Use this decorator on a function named `multiply` that takes two numbers and returns their product.

**Note**: The "function_cache.txt" file should only store unique input-output pairs.

**File Name**: `04_cache_result_decorator.py`

**Sample Input**:  
```python
multiply(2, 3)
multiply(4, 5)
multiply(2, 3)
```
**Sample Output**: 
- in the terminal:
```
6
20
6
```
- In "function_cache.txt":
```
(2, 3):6
(4, 5):20
```

---

### Exercise 5: Log Args Decorator (Simple)

Write a decorator named `log_args` that:  
1. Stores the function's arguments in a CSV file named "args_log.csv" (columns: "Function Name", "Arguments").  
2. Executes the original function without modification.  
3. Use this decorator on a function named `greet` that takes a name and a message and prints a greeting.

**File Name**: `05_log_args_decorator.py`

**Sample Input**:  
```python
greet("Ali", "Good morning")
greet("Sara", "Hello there")
```
**Sample Output**: 

- in the terminal:
```
Hello Ali, Good morning!
Hello Sara, Hello there!
```
- in "args_log.txt":
```
Function Name,Arguments
greet,"('Ali', 'Good morning')"
greet,"('Sara', 'Hello there')"
```
---

### Exercise 6: Retry on Failure Decorator (Intermediate)

Write a decorator named `retry_on_failure` that:  
1. Retries the function up to 3 times if it raises an exception, with a random delay between 0.5 and 1.5 seconds (using `time.sleep` and `random.uniform`).  
2. Logs each failed attempt to a text file named "retry_logs.txt" (including function name, error, and attempt number).  
3. Raises the last exception if all 3 attempts fail.  
4. Use this decorator on a function named `divide` that takes two numbers and returns their division (and may raise a division-by-zero error).

**File Name**: `06_retry_on_failure_decorator.py`

**Sample Input**:  
```python
divide(10, 2)
divide(5, 0)
```
**Sample Output**:

- in the terminal:
```
5.0
Traceback (most recent call last):
  File "...", line ..., in <module>
    divide(5, 0)
  File "...", line ..., in wrapper
    raise e
ZeroDivisionError: division by zero
```
- In "retry_logs.txt":
```
Attempt 1 for divide failed: division by zero
Attempt 2 for divide failed: division by zero
Attempt 3 for divide failed: division by zero
```

---

---

### Exercise 7: Restrict Access Decorator (Intermediate)

Write a decorator named `restrict_access` that:  
1. Checks if a user (passed as the `user` argument) is allowed based on a JSON file named "users.json" (containing a list of dictionaries with "username" and "allowed" keys).  
2. Prints an error message and skips the function if the user is not allowed.  
3. Logs every access attempt (successful or not) to a text file named "access_logs.txt" (including function name, user, and result: "allowed" or "denied").  
4. Use this decorator on a function named `get_secret` that prints a secret message.

**File Name**: `07_restrict_access_decorator.py`

**Sample Input**:  
```python
get_secret("admin")
get_secret("guest")
get_secret("unknown")
```
**Sample Output**:  

- in the terminal:
```
Top secret message!
Access denied: user 'guest' not allowed.
Access denied: user 'unknown' not allowed.
```
- In "access_logs.txt":
```
get_secret: admin - allowed
get_secret: guest - denied
get_secret: unknown - denied
```
---

### Exercise 8: Rate Limit Decorator (Intermediate)

Write a decorator named `rate_limit` that:  
1. Limits the number of function calls to 3 within a 60-second window.  
2. Stores call information (time and count) in a JSON file named "rate_limit.json" (with keys "function_name", "calls", and "last_reset").  
3. Prints an error message and skips the function if the call limit is exceeded.  
4. Use this decorator on a function named `say_hi` that prints a simple message.

**Note**: The counter should reset every 60 seconds.

**File Name**: `08_rate_limit_decorator.py`

**Sample Input**:  
```python
say_hi("Ali")
say_hi("Sara")
say_hi("Reza")
say_hi("Kasra")
```

**Sample Output**:  

- in the terminal:
```
Hi Ali!
Hi Sara!
Hi Reza!
Rate limit exceeded: maximum 3 calls per 60 seconds.
```
- In "rate_limit.json" (after execution):
```json
{
    "function_name": "say_hi",
    "calls": 3,
    "last_reset": 43147.1112435
}
```
---

### Exercise 9: Time Execution Decorator (Intermediate)

Write a decorator named `time_execution` that:  
1. Measures the execution time of a function (using `time.perf_counter`) and prints it in the terminal (format: "Execution time: X.XXX seconds").  
2. Logs each execution time in a CSV file named "execution_times.csv" (columns: "Function Name", "Execution Time", "Timestamp").  
3. Prints a warning if the execution time exceeds 1 second ("Warning: execution took longer than 1 second!").  
4. Use this decorator on a function named `slow_add` that adds two numbers with an artificial 1.5-second delay (using `time.sleep`).

**File Name**: `09_time_execution_decorator.py`

**Sample Input**:  
```python
slow_add(5, 3)
slow_add(2, 4)
```
**Sample Input**: 

- in the terminal:
```
Execution time: 1.5XX seconds
Warning: execution took longer than 1 second!
Execution time: 1.5XX seconds
Warning: execution took longer than 1 second!
```
- In "execution_times.csv":
```csv
Function Name,Execution Time,Timestamp
slow_add,1.5XX,1712019600.0
slow_add,1.5XX,1712019602.0
```
---

### Exercise 10: Cache with Expiry Decorator (Intermediate)

Write a decorator named `cache_with_expiry` that:  
1. Caches the function result to avoid re-execution, with an expiry time of 30 seconds.  
2. Stores cache data (inputs, outputs, and storage time) in a JSON file named "cache_data.json" (keys: "function_name", "args", "result", "timestamp").  
3. Ignores the cache and re-executes the function if the expiry time has passed.  
4. Use this decorator on a function named `multiply` that multiplies two numbers with an artificial 1-second delay (using `time.sleep`).

**File Name**: `10_cache_with_expiry_decorator.py`

**Sample Input**:  
```python
multiply(2, 3)
multiply(2, 3)  // should use cache
multiply(4, 5)
```
**Sample Output**: 

- in the terminal:
```
Calculating: 2 * 3
6
From cache: 2 * 3
6
Calculating: 4 * 5
20
```
- In "cache_data.json" (after execution):
```json
{
    "cache": [
        {"function_name": "multiply", "args": [2, 3], "result": 6, "timestamp": 1712019600.0},
        {"function_name": "multiply", "args": [4, 5], "result": 20, "timestamp": 1712019601.0}
    ]
}
```

---

### Exercise 11: Advanced Logger Decorator (Hard)

Write a decorator named `advanced_logger` that:  
1. Implements an advanced logging system with levels (INFO, WARNING, ERROR).  
2. Logs messages to a text file named "app_logs.txt" in the format: `[level] [ISO timestamp] [function_name] message`.  
3. Logs exceptions as ERROR and re-raises them.  
4. Tracks the count of each log level in a JSON file named "log_stats.json" (keys: "INFO", "WARNING", "ERROR").  
5. Use this decorator on a function named `divide_numbers` that divides two numbers and:  
   - Logs a WARNING if the result exceeds 10.  
   - Logs an ERROR if division by zero occurs.

**File Name**: `11_advanced_logger_decorator.py`

**Sample Input**:  
```python
divide_numbers(20, 2)  // result > 10, should log WARNING
divide_numbers(5, 2)   // normal, should log INFO
divide_numbers(10, 0)  // division by zero, should log ERROR
```
**Sample Output**:  

- in the terminal:
```
Traceback (most recent call last):
  File "...", line ..., in <module>
    divide_numbers(10, 0)
  File "...", line ..., in wrapper
    raise e
ZeroDivisionError: division by zero
```
- In "app_logs.txt":
```
[WARNING] 2025-04-07T12:00:00Z [divide_numbers] Result exceeds 10: 10.0
[INFO] 2025-04-07T12:00:01Z [divide_numbers] Function executed successfully
[ERROR] 2025-04-07T12:00:02Z [divide_numbers] division by zero
```
- In "log_stats.json":
```json
{
    "INFO": 1,
    "WARNING": 1,
    "ERROR": 1
}
```
---

### Exercise 12: Retry with Backoff Decorator (Hard)

Write a decorator named `retry_with_backoff` that:  
1. Retries a function up to 3 times if it raises an error.  
2. Applies an exponential backoff delay between retries: 1s, 2s, 4s.  
3. Logs all attempts to "retry_logs.txt" in the format: `[ISO timestamp] [function_name] message`.  
4. Raises the last error if all attempts fail, logging "All attempts failed".  
5. Tracks success and failure counts in "retry_stats.json" (keys: "success", "failure").  
6. Use this decorator on a function named `unstable_operation` that:  
   - Generates a random number (0-1) and raises ValueError if < 0.7.

**File Name**: `12_retry_with_backoff_decorator.py`

**Sample Input**:  
```python
unstable_operation()
```
**Sample Output**: 

- in the terminal:
```
Traceback (most recent call last):
  File "...", line ..., in <module>
    unstable_operation()
  File "...", line ..., in wrapper
    raise last_error
ValueError: Operation failed
```
- In "retry_logs.txt":
```
[2025-04-07T12:00:00Z] [unstable_operation] Attempt 1 failed with error: Operation failed - Retrying in 1 seconds
[2025-04-07T12:00:01Z] [unstable_operation] Attempt 2 failed with error: Operation failed - Retrying in 2 seconds
[2025-04-07T12:00:03Z] [unstable_operation] Attempt 3 failed with error: Operation failed - All attempts failed
```
- In "retry_stats.json":
```json
{
    "success": 0,
    "failure": 1
}
```
---

### Exercise 13: Restrict Access Decorator (Hard)

Write a decorator named `restrict_access` that:  
1. Restricts function access based on user role ("admin", "editor", "viewer").  
2. Allows only specified roles, raising `PermissionError` for others ("Access denied: insufficient permissions").  
3. Logs access attempts to "access_logs.txt" in the format: `[ISO timestamp] [function_name] [role] Access [granted|denied]`.  
4. Tracks granted/denied counts per role in "access_stats.json" (keys: roles, subkeys: "granted", "denied").  
5. Use this decorator on a function named `modify_data` that:  
   - Is allowed only for "admin" role.  
   - Prints "Data modified successfully".

**File Name**: `13_restrict_access_decorator.py`

**Sample Input**:  
```python
for role in ["admin", "editor", "viewer"]:
    try:
        modify_data(role)
    except PermissionError as e:
        print(f"Error for {role}: {e}")
```
**Sample Input**:

- in the terminal:
```
Data modified successfully
Error for editor: Access denied: insufficient permissions
Error for viewer: Access denied: insufficient permissions
```
- In "access_logs.txt":
```
[2025-04-07T12:00:00Z] [modify_data] [admin] Access granted
[2025-04-07T12:00:01Z] [modify_data] [editor] Access denied
[2025-04-07T12:00:02Z] [modify_data] [viewer] Access denied
```
- In "access_stats.json":
```json
{
    "admin": {"granted": 1, "denied": 0},
    "editor": {"granted": 0, "denied": 1},
    "viewer": {"granted": 0, "denied": 1}
}
```
---

### Exercise 14: Rate Limiter Decorator (Hard)

Write a decorator named `rate_limiter` that:  
1. Limits the number of function calls within a time window (e.g., 60 seconds).  
2. Takes a call limit (e.g., 5) as an argument and raises `RuntimeError` ("Rate limit exceeded") if exceeded.  
3. Logs attempts to "rate_limit_logs.txt" in the format: `[ISO timestamp] [function_name] Call #X within window - [allowed|blocked]`.  
4. Tracks allowed/blocked counts in "rate_limit_stats.json" (keys: "allowed", "blocked").  
5. Use this decorator on a function named `fetch_data` that:  
   - Prints "Data fetched successfully".  
   - Has a limit of 5 calls in 60 seconds.

**File Name**: `14_rate_limiter_decorator.py`

**Sample Input**:  
```python
for _ in range(7):
    try:
        fetch_data()
    except RuntimeError as e:
        print(f"Error: {e}")
```
**Sample Output**:  

- In the terminal:
```
Data fetched successfully
Data fetched successfully
Data fetched successfully
Data fetched successfully
Data fetched successfully
Error: Rate limit exceeded
Error: Rate limit exceeded
```
- In "rate_limit_logs.txt":
```
[2025-04-07T12:00:00Z] [fetch_data] Call #1 within window - allowed
[2025-04-07T12:00:01Z] [fetch_data] Call #2 within window - allowed
[2025-04-07T12:00:02Z] [fetch_data] Call #3 within window - allowed
[2025-04-07T12:00:03Z] [fetch_data] Call #4 within window - allowed
[2025-04-07T12:00:04Z] [fetch_data] Call #5 within window - allowed
[2025-04-07T12:00:05Z] [fetch_data] Call #6 within window - blocked
[2025-04-07T12:00:06Z] [fetch_data] Call #7 within window - blocked
```
- In "rate_limit_stats.json":
```json
{
    "allowed": 5,
    "blocked": 2
}
```
---

### Exercise 15: Retry on Failure Decorator (Hard)

Write a decorator named `retry_on_failure` that:  
1. Retries a function on any exception up to a specified number of times (e.g., 3).  
2. Takes two arguments: `max_retries` (max attempts) and `delay` (seconds between retries).  
3. Raises the last exception if all retries fail.  
4. Logs each attempt to "retry_logs.txt" in the format: `[ISO timestamp] [function_name] Attempt #X - [success|failure: ExceptionType: message]`.  
5. Use this decorator on a function named `unreliable_operation` that:  
   - Generates a random number (0-9).  
   - Raises `ValueError` ("Operation failed") if the number > 4, otherwise prints "Operation succeeded" and returns the number.  

**File Name**: `15_retry_on_failure_decorator.py`

**Sample Input**:  
```python
try:
    unreliable_operation()
except ValueError as e:
    print(f"Final error after retries: {e}")
```
**Sample Output**: 

- In the terminal:
```
Operation succeeded
```
- In "retry_logs.txt":
```
[2025-04-07T12:00:00Z] [unreliable_operation] Attempt #1 - failure: ValueError: Operation failed
[2025-04-07T12:00:02Z] [unreliable_operation] Attempt #2 - success
```
