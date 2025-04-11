# Generators Exercises

In this directory, we explore Python generators through a series of 15 exercises: 5 easy, 5 medium, and 5 hard. Generators are functions that use `yield` to produce a sequence of values lazily, one at a time, instead of storing them all in memory. These exercises aim to build understanding of generators, from simple counting sequences to more complex applications, with each solution saved as a separate `.py` file and tested with sample inputs.

---

### Exercise 1: Count Up Generator (Easy)

Write a generator named `count_up` that:  
1. Takes a starting number (`start`) as an argument.  
2. Counts up indefinitely from that number (e.g., 5, 6, 7, ...).  
3. Prints the first 5 values to test it.

**File Name**: `01_count_up_generator.py`

**Sample Input**:  
```python
counter = count_up(5)
for _ in range(5):
    print(next(counter))
```
**Sample Output**:
```
5
6
7
8
9
```
---

### Exercise 2: Even Numbers Generator (Easy)

Write a generator named `even_numbers` that:  
1. Starts from 0 and generates even numbers indefinitely (e.g., 0, 2, 4, 6, ...).  
2. Prints the first 6 values to test it.

**File Name**: `02_even_numbers_generator.py`

**Sample Input**:  
```python
evens = even_numbers()
for _ in range(6):
    print(next(evens))
```
**Sample Output**:
```
0
2
4
6
8
10
```
---

### Exercise 3: Squares Generator (Easy)

Write a generator named `squares` that:  
1. Starts from 1 and generates the squares of natural numbers indefinitely (e.g., 1, 4, 9, 16, ...).  
2. Prints the first 5 values to test it.

**File Name**: `03_squares_generator.py`

**Sample Input**:  
```python
squares_gen = squares()
for _ in range(5):
    print(next(squares_gen))
```
**Sample Output**: 
```
1
4
9
16
25
```
---

### Exercise 4: Fibonacci Generator (Easy)

Write a generator named `fibonacci` that:  
1. Generates the Fibonacci sequence indefinitely (e.g., 0, 1, 1, 2, 3, 5, 8, ...).  
2. Prints the first 7 values to test it.

**File Name**: `04_fibonacci_generator.py`

**Sample Input**:  
```python
fib = fibonacci()
for _ in range(7):
    print(next(fib))
```
**Sample Output**:
```
0
1
1
2
3
5
8
```
---

### Exercise 5: Powers of Two Generator (Easy)

Write a generator named `powers_of_two` that:  
1. Starts from 1 and generates powers of 2 indefinitely (e.g., 1, 2, 4, 8, 16, ...).  
2. Prints the first 6 values to test it.

**File Name**: `05_powers_of_two_generator.py`

**Sample Input**:  
```python
powers = powers_of_two()
for _ in range(6):
    print(next(powers))
```
**Sample Output**:
```
1
2
4
8
16
32
```
---

### Exercise 6: Limited Range Generator (Medium)

Write a generator named `limited_range` that:  
1. Takes three arguments: `start` (beginning), `stop` (end), and `step` (increment).  
2. Generates a sequence from `start` up to (but not including) `stop` with the given `step`.  
3. Stops when it reaches or exceeds `stop`.  
4. Test it with `start=2`, `stop=10`, `step=3` and print all values.

**File Name**: `06_limited_range_generator.py`

**Sample Input**:  
```python
for num in limited_range(2, 10, 3):
    print(num)
```
**Sample Output**: 
```
2
5
8
```
---

### Exercise 7: Cycle List Generator (Medium)

Write a generator named `cycle_list` that:  
1. Takes a list as an argument (e.g., `[1, 2, 3]`) and cycles through its elements indefinitely.  
2. Repeats the list from the beginning when it reaches the end (e.g., 1, 2, 3, 1, 2, 3, ...).  
3. Test it with the list `[1, 2, 3]` and print the first 10 values.

**File Name**: `07_cycle_list_generator.py`

**Sample Input**:  
```python
cycler = cycle_list([1, 2, 3])
for _ in range(10):
    print(next(cycler))
```
**Sample Output**:  
```
1
2
3
1
2
3
1
2
3
1
```
---

### Exercise 8: Filter Odds Generator (Medium)

Write a generator named `filter_odds` that:  
1. Takes another generator as an argument (e.g., one producing natural numbers).  
2. Filters out odd numbers and yields only even numbers.  
3. For testing, create a generator `natural_numbers` that produces natural numbers starting from 1 (1, 2, 3, 4, ...).  
4. Use `filter_odds` with `natural_numbers()` and print the first 5 values.

**File Name**: `08_filter_odds_generator.py`

**Sample Input**:  
```python
naturals = natural_numbers()
evens = filter_odds(naturals)
for _ in range(5):
    print(next(evens))
```
**Sample Output**:
```
2
4
6
8
10
```
