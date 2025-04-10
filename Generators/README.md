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
