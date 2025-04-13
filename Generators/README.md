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
---

### Exercise 9: Unique Values Generator (Medium)

Write a generator named `unique_values` that:  
1. Takes a list as an argument (e.g., `[1, 2, 2, 3, 3, 4, 1]`) and yields only unique values in their order of appearance.  
2. Skips duplicates, yielding each value only the first time it appears.  
3. Test it with the list `[1, 2, 2, 3, 3, 4, 1]` and print all values.

**File Name**: `09_unique_values_generator.py`

**Sample Input**:  
```python
for num in unique_values([1, 2, 2, 3, 3, 4, 1]):
    print(num)
```
**Sample Output**:
```
1
2
3
4
```
---

### Exercise 10: Running Sum Generator (Medium)

Write a generator named `running_sum` that:  
1. Takes another generator as an argument (e.g., one producing numbers).  
2. Yields the running sum of the values produced by the input generator.  
3. For testing, create a generator `count_up` that produces natural numbers starting from 1 (1, 2, 3, 4, ...).  
4. Use `running_sum` with `count_up()` and print the first 6 values.

**File Name**: `10_running_sum_generator.py`

**Sample Input**:  
```python
counter = count_up()
sums = running_sum(counter)
for _ in range(6):
    print(next(sums))
```
**Sample Output**:
```
1
3
6
10
15
21
```
---

### Exercise 11: Flatten Nested Generator (Hard)

Write a generator named `flatten_nested` that:  
1. Takes a nested list as an argument (e.g., `[1, [2, [3, 4], 5], [6]]`), which may contain numbers and nested lists of any depth.  
2. Yields all numbers in a flat sequence, in their order of appearance.  
3. Assumes non-list elements are numbers.  
4. Test it with the list `[1, [2, [3, 4], 5], [6]]` and print all values.

**File Name**: `11_flatten_nested_generator.py`

**Sample Input**:  
```python
for num in flatten_nested([1, [2, [3, 4], 5], [6]]):
    print(num)
```
**Sample Output**:
```
1
2
3
4
5
6
```
---
### Exercise 12: Prime Numbers Generator (Hard)

Write a generator named `prime_numbers` that:  
1. Generates prime numbers indefinitely (e.g., 2, 3, 5, 7, 11, ...).  
2. Uses an efficient method to check for primality, such as testing divisibility only up to the square root of the number and skipping even numbers after 2.  
3. Prints the first 6 values to test it.

**File Name**: `12_prime_numbers_generator.py`

**Sample Input**:  
```python
primes = prime_numbers()
for _ in range(6):
    print(next(primes))
```
**Sample Output**:
```
2
3
5
7
11
13
```
---
### Exercise 13: File Lines Generator (Hard)

Write a generator named `file_lines` that:  
1. Takes a text file name (e.g., `data.txt`) and a keyword as arguments.  
2. Yields lines from the file one by one, but only those containing the keyword.  
3. The search must be case-insensitive.  
4. If the file is not found, the generator should yield `"File not found"` once and then stop.  
5. For testing, assume `data.txt` has the following content:
**data.txt**:
```
Hello world
This is a Test
Python programming
Another test line
```
Test it with the keyword `test` and print all matching lines.

**File Name**: `13_file_lines_generator.py`

**Sample Input**:  
```python
for line in file_lines("data.txt", "test"):
 print(line.strip())
```
**Sample Output**: 
```
This is a Test
Another test line
```
**If the file does not exist**:
```python
for line in file_lines("notfound.txt", "test"):
    print(line.strip())
```
**Sample Output**: 
```
File not found
```
---
### Exercise 14: Chained Generators (Hard)

Write a generator named `chained_generators` that:  
1. Takes a list of generators as an argument (e.g., `[gen1, gen2, gen3]`).  
2. Yields all values produced by these generators one by one, in order: all values from the first generator, then the second, and so on.  
3. Skips any empty generators (those producing no values) and moves to the next.  
4. For testing, create three sample generators:  
   - `count_up`: Produces numbers from 1 to 3 (i.e., 1, 2, 3).  
   - `squares`: Produces squares of numbers 1 and 2 (i.e., 1, 4).  
   - `evens`: Produces even numbers from 2 to 6 (i.e., 2, 4, 6).  
   Print all values produced by `chained_generators` with these generators.

**File Name**: `14_chained_generators.py`

**Sample Input**:  
```python
def count_up():
    for i in range(1, 4):
        yield i

def squares():
    for i in range(1, 3):
        yield i * i

def evens():
    for i in range(2, 7, 2):
        yield i

generators = [count_up(), squares(), evens()]
for value in chained_generators(generators):
    print(value)
```
**Sample Output**:  
```
1
2
3
1
4
2
4
6
```
---
### Exercise 15: Infinite Filter Generator (Hard)

Write a generator named `infinite_filter` that:  
1. Takes an input generator (e.g., one producing numbers) and a predicate function as arguments.  
2. Yields only the values from the input generator for which the predicate function returns `True`.  
3. The generator should work indefinitely (as long as the input generator produces values).  
4. For testing, create a sample generator named `natural_numbers` that produces natural numbers starting from 1 (1, 2, 3, ...).  
5. Create a predicate function named `is_multiple_of_3` that checks if a number is divisible by 3.  
6. Using `infinite_filter` with these, print the first 5 numbers that are multiples of 3.

**File Name**: `15_infinite_filter_generator.py`

**Sample Input**:  
```python
def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

def is_multiple_of_3(n):
    return n % 3 == 0

filtered = infinite_filter(natural_numbers(), is_multiple_of_3)
for _ in range(5):
    print(next(filtered))
```
**Sample Output**:
```
3
6
9
12
15
```
---
