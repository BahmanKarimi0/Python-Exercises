# Functions Exercises
This section is dedicated to exploring and practicing Python functions through a series of 20 exercises. The exercises are divided into four levels of difficulty: 5 simple, 5 medium, 5 hard, and 5 challenging. Each exercise focuses on building and strengthening skills in defining functions, handling inputs/outputs, and solving problems with increasing complexity. The goal is to master function creation and usage while tackling practical programming scenarios.

---

### Exercise 01: Power Function (Simple)
**Question:**  
Write a function `power(base, exp)` that calculates `base` raised to the power of `exp` using only multiplication (no `**` or `pow`). Assume `exp` is a non-negative integer.

**Solution:** See `01_power.py`.

---

### Exercise 02: Prime Number Check (Simple)
**Question:**  
Write a function `is_prime(n)` that takes a positive integer `n` (>1) and returns `True` if it’s a prime number, and `False` otherwise.

**Solution:** See `02_is_prime.py`.

---

### Exercise 03: Reverse String (Simple)
**Question:**  
Write a function `reverse_string(s)` that takes a string `s` and returns its reverse, using only loops or simple operations (no `[::-1]` or `reversed`).

**Solution:** See `03_reverse_string.py`.

---

### Exercise 04: Sum of Digits (Simple)
**Question:**  
Write a function `sum_of_digits(n)` that takes a positive integer `n` and returns the sum of its digits. You can use string conversion.

**Solution:** See `04_sum_of_digits.py`.

---

### Exercise 05: Count Vowels (Simple)
**Question:**  
Write a function `count_vowels(s)` that takes a string `s` and returns the number of vowels (a, e, i, o, u), treating uppercase and lowercase letters the same.

**Solution:** See `05_count_vowels.py`.

---

### Exercise 06: Find Maximum in List (Medium)
**Question:**  
Write a function `find_max(numbers)` that takes a list of numbers and returns the largest number in it, without using the `max()` function. Assume the list is non-empty and contains only numbers.

**Solution:** See `06_find_max.py`.

---

### Exercise 07: Reverse Words in Sentence (Medium)
**Question:**  
Write a function `reverse_words(sentence)` that takes a sentence and returns it with the words in reverse order, while keeping the letters in each word unchanged, without using `[::-1]` for reversing the word list. Assume words are separated by single spaces with no extra spaces.

**Solution:** See `07_reverse_words.py`.

---

### Exercise 08: Count Duplicates in List (Medium)
**Question:**  
Write a function `count_duplicates(words)` that takes a list of strings and returns a dictionary with the count of each word, treating uppercase and lowercase letters the same.

**Solution:** See `08_count_duplicates.py`.

---

### Exercise 09: Filter Even Numbers (Medium)
**Question:**  
Write a function `filter_even_numbers(numbers)` that takes a list of integers and returns a new list containing only the even numbers, without using the `filter()` function. Return an empty list if no even numbers are found.

**Solution:** See `09_filter_even_numbers.py`.

---

### Exercise 10: Sum Subsets (Medium)
**Question:**  
Write a function `sum_subsets(numbers, target)` that takes a list of numbers and a target number, and returns `True` if a subset of the numbers can sum to the target, and `False` otherwise.

**Solution:** See `10_sum_subsets.py`.

---

### Exercise 11: Limited Factorial (Hard)
**Question:**  
Write a function `limited_factorial(n, limit)` that calculates the factorial of `n`, but if the result exceeds a specified `limit`, it returns the `limit` instead. Assume `n` is a non-negative integer and `limit` is a positive integer. Use a loop and do not use recursion or built-in functions like `math.factorial`.

**Examples:**  
- `limited_factorial(5, 50)` → `50` (since 5! = 120 and 120 > 50, return 50)  
- `limited_factorial(5, 10)` → `10` (since 5! = 120 and 120 > 10, return 10)  
- `limited_factorial(4, 25)` → `24` (since 4! = 24 and 24 > 25 is false, return 24)

**Solution:** See `11_limited_factorial.py`.

---

