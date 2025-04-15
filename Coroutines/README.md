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
```
Received string #1: apple
Received string #2: banana
Received string #3: cherry
Received string #4: date
```
