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
---
### Exercise 6: File Logger Coroutine (Medium)

Write a coroutine named `file_logger` that:  
1. Takes a file path (e.g., `"logs.txt"`) and indefinitely receives dictionaries from outside using `yield`. Each dictionary contains `"message"` (string) and `"level"` (string, e.g., `"INFO"`, `"ERROR"`).  
2. Saves each dictionary as a line in the text file (e.g., `level|message`).  
3. Keeps an internal list of all received `"level"` values and, if the string `"count"` is sent, yields a dictionary with the count of each `"level"` (e.g., `{"INFO": 2, "ERROR": 1}`).  
4. For testing:  
   - Create a separate generator producing 3 sample dictionaries (e.g., `{"message": "System started", "level": "INFO"}`, ...).  
   - Start the coroutine, send dictionaries from the generator, then send `"count"` and print the result.

**File Name**: `06_file_logger_coroutine.py**

**Sample Input**:  
```python
def sample_logs():
    yield {"message": "System started", "level": "INFO"}
    yield {"message": "Failed to connect", "level": "ERROR"}
    yield {"message": "User logged in", "level": "INFO"}

l = file_logger("logs.txt")
next(l)  # Start the coroutine
for log in sample_logs():
    l.send(log)
print(l.send("count"))
```
**Sample Output**:

- In the teminal:
```
{'INFO': 2, 'ERROR': 1}
```
- In logs.txt:
```
INFO|System started
ERROR|Failed to connect
INFO|User logged in
```
---
### Exercise 7: Key-Value Logger Coroutine (Medium)

Write a coroutine named `keyval_logger` that:  
1. Takes a text file path (e.g., `"keyval.txt"`) and indefinitely receives dictionaries from outside using `yield`. Each dictionary contains `"key"` (string) and `"value"` (number).  
2. Saves each dictionary as a line in the text file, formatted as `key=value` (e.g., `user1=100`).  
3. Keeps an internal dictionary of keys and values and, if the string `"total"` is sent, yields the sum of all values.  
4. For testing:  
   - Create a separate generator producing 3 sample dictionaries (e.g., `{"key": "user1", "value": 100}`, ...).  
   - Start the coroutine, send dictionaries from the generator, then send `"total"` and print the result.

**File Name**: `07_keyval_logger_coroutine.py`

**Sample Input**:  
```python
def sample_dicts():
    yield {"key": "user1", "value": 100}
    yield {"key": "user2", "value": 200}
    yield {"key": "user3", "value": 300}

k = keyval_logger("keyval.txt")
next(k)  # Start the coroutine
for d in sample_dicts():
    k.send(d)
print(k.send("total"))
```
**Sample Input**: 

- In the terminal:
```
600
```
- In the keyval.txt:
```
user1=100
user2=200
user3=300
```
---
### Exercise 8: List Accumulator Coroutine (Medium)

Write a coroutine named `list_accumulator` that:  
1. Takes a text file path (e.g., `"accum.txt"`) and indefinitely receives lists of numbers from outside using `yield`.  
2. Saves each list as a line in the text file, formatted as a comma-separated string (e.g., `1,2,3`).  
3. Keeps an internal list of all received numbers and, if the string `"average"` is sent, yields the average of the numbers.  
4. For testing:  
   - Create a separate generator producing 3 sample lists (e.g., `[1, 2]`, `[3]`, `[4, 5]`).  
   - Start the coroutine, send lists from the generator, then send `"average"` and print the result.

**File Name**: `08_list_accumulator_coroutine.py`

**Sample Input**:  
```python
def sample_lists():
    yield [1, 2]
    yield [3]
    yield [4, 5]

a = list_accumulator("accum.txt")
next(a)  # Start the coroutine
for lst in sample_lists():
    a.send(lst)
print(a.send("average"))
```
**Sample Output**: 

- In the terminal:
```
3.0
```
- In accum.txt:
```
1,2 
3 
4,5 
```
---
### Exercise 9: Tuple Filter Coroutine (Medium)

Write a coroutine named `tuple_filter` that:  
1. Takes a text file path (e.g., `"filtered.txt"`) and a threshold number (e.g., `threshold`, float) and indefinitely receives 2-tuples (containing a string and a number) from outside using `yield`.  
2. If the number in the tuple is greater than or equal to the threshold, saves the tuple as a line in the text file, formatted as `string:number` (e.g., `item1:10.5`).  
3. Keeps an internal list of strings from saved tuples and, if the string `"count"` is sent, yields the number of saved tuples.  
4. For testing:  
   - Create a separate generator producing 4 sample tuples (e.g., `("item1", 10.5)`, ...).  
   - Start the coroutine, send tuples from the generator, then send `"count"` and print the result.

**File Name**: `09_tuple_filter_coroutine.py`

**Sample Input**:  
```python
def sample_tuples():
    yield ("item1", 10.5)
    yield ("item2", 5.0)
    yield ("item3", 15.0)
    yield ("item4", 7.5)

f = tuple_filter("filtered.txt", 8.0)
next(f)  # Start the coroutine
for tup in sample_tuples():
    f.send(tup)
print(f.send("count"))
```
**Sample Output**:

- In the terminal:
```
Invalid tuple
Invalid tuple
2
```
- In 'filtered.txt':
```
item1:10.5
item3:15.0
```
---
### Exercise 10: JSON Processor Coroutine (Medium)

Write a coroutine named `json_processor` that:  
1. Takes a text file path (e.g., `"processed.txt"`) and indefinitely receives dictionaries from outside using `yield`. Each dictionary must contain `"id"` (string) and `"data"` (list of numbers).  
2. Saves each dictionary as a line in the text file, formatted as `id:data_sum` (e.g., `record1:15.5`), where `data_sum` is the sum of numbers in `"data"`.  
3. Keeps an internal dictionary mapping each `"id"` to the maximum `data_sum` and, if the string `"max"` is sent, yields the internal dictionary.  
4. For testing:  
   - Create a separate generator producing 3 sample dictionaries (e.g., `{"id": "record1", "data": [1, 2, 3]}`, ...).  
   - Start the coroutine, send dictionaries from the generator, then send `"max"` and print the result.

**File Name**: `10_json_processor_coroutine.py`

**Sample Input**:  
```python
def sample_dicts():
    yield {"id": "record1", "data": [1, 2, 3]}
    yield {"id": "record2", "data": [4, 5]}
    yield {"id": "record1", "data": [10]}

p = json_processor("processed.txt")
next(p)  # Start the coroutine
for d in sample_dicts():
    p.send(d)
print(p.send("max"))
```
**Sample Output**:

- In the terminal:
```
{'record1': 10, 'record2': 9}
```
- In 'processed.txt':
```
record1:6
record2:9
record1:10
```
---
