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
