# Coroutines Exercises

This directory contains a series of Python coroutine exercises to explore their ability to receive, process, and manage data flows. Coroutines extend generators by allowing two-way communication (sending and receiving values) using `yield`. In this collection, we implement 15 exercises: 5 simple, 5 medium, and 5 hard. The simple exercises focus on basic coroutine mechanics like receiving values and maintaining state, while medium and hard exercises dive into advanced patterns like chaining coroutines or using `asyncio` for asynchronous programming. Each exercise is saved as a separate `.py` file with sample inputs for testing.

---

### Exercise 1: Simple Receiver Coroutine (Simple)

Write a coroutine named `receiver` that:  
1. Indefinitely receives values (e.g., strings or numbers) from outside using `yield`.  
2. Prints each received value with a message indicating it was received (e.g., `"Received: value"`).  
3. For testing, start the coroutine and send 3 arbitrary values (e.g., `"hello"`, `42`, `"world"`).

**File Name**: `01_receiver_coroutine.py`

**Sample Input**:  
```python
r = receiver()
next(r)  # Start the coroutine
r.send("hello")
r.send(42)
r.send("world")
```
**Sample Output**:
```
Received: hello
Received: 42
Received: world
```
---
### Exercise 2: Counter Coroutine (Simple)

Write a coroutine named `counter` that:  
1. Indefinitely receives strings from outside using `yield`.  
2. Keeps track of the number of strings received and prints each with its count (e.g., `"Received string #N: string"`, where `N` is the count).  
3. For testing, start the coroutine and send 4 arbitrary strings (e.g., `"apple"`, `"banana"`, `"cherry"`, `"date"`).

**File Name**: `02_counter_coroutine.py`

**Sample Input**:  
```python
c = counter()
next(c)  # Start the coroutine
c.send("apple")
c.send("banana")
c.send("cherry")
c.send("date")
```
**Sample Output**:
```
Received string #1: apple
Received string #2: banana
Received string #3: cherry
Received string #4: date
```
---
### Exercise 3: Accumulator Coroutine (Simple)

Write a coroutine named `accumulator` that:  
1. Indefinitely receives numbers (e.g., integers or floats) from outside using `yield`.  
2. Keeps track of the sum of numbers received and prints the current sum each time (e.g., `"Current sum: sum"`).  
3. For testing, start the coroutine and send 4 arbitrary numbers (e.g., `10`, `20.5`, `30`, `40.75`).

**File Name**: `03_accumulator_coroutine.py`

**Sample Input**:  
```python
a = accumulator()
next(a)  # Start the coroutine
a.send(10)
a.send(20.5)
a.send(30)
a.send(40.75)
```
**Sample Output**:
```
Current sum: 10
Current sum: 30.5
Current sum: 60.5
Current sum: 101.25
```
---
### Exercise 4: Echo Coroutine (Simple)

Write a coroutine named `echo` that:  
1. Indefinitely receives values (e.g., strings or numbers) from outside using `yield`.  
2. Yields back each received value as output (i.e., returns the same value).  
3. For testing, start the coroutine and send 3 arbitrary values (e.g., `"test"`, `100`, `3.14`) and print the returned values.

**File Name**: `04_echo_coroutine.py`

**Sample Input**:  
```python
e = echo()
next(e)  # Start the coroutine
print(e.send("test"))
print(e.send(100))
print(e.send(3.14))
```
**Sample Output**:
```
test
100
3.14
```
---
### Exercise 5: Logger Coroutine (Simple)

Write a coroutine named `logger` that:  
1. Indefinitely receives strings from outside using `yield`.  
2. Adds each received string to an internal list and prints the current count of stored strings (e.g., `"Logged string, total: N"`, where `N` is the count).  
3. For testing, start the coroutine and send 3 arbitrary strings (e.g., `"error"`, `"warning"`, `"info"`).

**File Name**: `05_logger_coroutine.py`

**Sample Input**:  
```python
l = logger()
next(l)  # Start the coroutine
l.send("error")
l.send("warning")
l.send("info")
```
**Sample Input**:
```
Logged string, total: 1
Logged string, total: 2
Logged string, total: 3
```
