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

### Exercise 12: Greatest Common Divisor of Strings (Hard)
**Question:**  
Write a function `gcd_strings(s1, s2)` that takes two strings `s1` and `s2` and returns the largest string that divides both `s1` and `s2` completely (i.e., both strings can be formed by repeating that string an integer number of times). If no such string exists, return an empty string `""`. Assume the inputs are non-empty strings containing only English letters. Do not use built-in functions like `math.gcd`.

**Examples:**  
- `gcd_strings("ABCABC", "ABC")` → `"ABC"`  
- `gcd_strings("ABABAB", "ABAB")` → `"AB"`  
- `gcd_strings("LEET", "CODE")` → `""`  
- `gcd_strings("AB", "ABABABABAB")` → `"AB"`

**Solution:** See `12_gcd_strings.py`.

---

### Exercise 13: Most Frequent Words in Text (Hard)
**Question:**  
Write a function `most_frequent_words(text, k)` that takes a string `text` and an integer `k`, and returns a list of the `k` most frequent words in the text. Words are separated by spaces, and the text contains only lowercase English letters and spaces. The output should be sorted by frequency in descending order. If there are fewer unique words than `k`, return all unique words.

**Examples:**  
- `most_frequent_words("the cat and the dog and the mouse", 2)` → `["the", "and"]`  
- `most_frequent_words("data data science is cool", 3)` → `["data", "science", "is"]`  
- `most_frequent_words("hello", 1)` → `["hello"]`  
- `most_frequent_words("a a a b b c", 2)` → `["a", "b"]`

**Constraints:**  
- `1 <= len(text) <= 1000`
- `1 <= k <= number of unique words`
- Text contains only lowercase English letters and spaces.

**File:** `13_most_frequent_words.py`

---

### Exercise 14: Moving Average (Hard)
**Question:**  
Write a function `moving_average(numbers, window)` that takes a list of numbers `numbers` and an integer `window`, and returns the moving average of the list with the specified window size. The moving average is computed as the average of `window` consecutive elements starting at each position. The output should be a list of averages, rounded to 2 decimal places. Ignore positions where the window exceeds the remaining elements.

**Examples:**  
- `moving_average([1, 2, 3, 4, 5], 3)` → `[2.00, 3.00, 4.00]`  
- `moving_average([1.5, 2.5, 3.5], 2)` → `[2.00, 3.00]`  
- `moving_average([1, 2], 1)` → `[1.00, 2.00]`  
- `moving_average([10, 20, 30], 4)` → `[]`

**Constraints:**  
- `1 <= len(numbers) <= 1000`
- `1 <= window <= len(numbers)`
- Numbers can be integers or floats.

**File:** `14_moving_average.py`

---

### Exercise 15: Find Repeated Patterns (Hard)
**Question:**  
Write a function `find_repeated_patterns(numbers, k)` that takes a list of numbers `numbers` and an integer `k`, and returns a list of all contiguous patterns of length `k` that appear at least twice in the list. Each pattern is itself a list of numbers. The order of patterns in the output doesn't matter.

**Examples:**  
- `find_repeated_patterns([1, 2, 3, 1, 2, 3, 4], 3)` → `[[1, 2, 3]]`  
- `find_repeated_patterns([1.5, 2.5, 1.5, 2.5, 3.5], 2)` → `[[1.5, 2.5]]`  
- `find_repeated_patterns([1, 2, 1, 2, 1, 2], 2)` → `[[1, 2]]`  
- `find_repeated_patterns([1, 2, 3, 4], 2)` → `[]`

**Constraints:**  
- `1 <= len(numbers) <= 1000`
- `1 <= k <= len(numbers)`
- Numbers can be integers or floats.

**File:** `15_find_repeated_patterns.py`

---

### Exercise 16: Count Words from File (Challenging)
**Question:**  
Write a function `count_words(filename)` that takes a filename (string), reads a text file, and returns a dictionary with words as keys and their counts as values. Convert all words to lowercase, ignore non-alphanumeric characters, and return a dictionary with an "error" key containing the error message if the file cannot be read.

**Examples:**  
- File `sample.txt`:
- `Hello world`
- `Hello Python hello`
- `World123`

→ `{"hello": 3, "world": 2, "python": 1, "world123": 1}`  
- File not found → `{"error": "File not found"}`

**Constraints:**  
- File has at most 1000 lines.
- Each line has at most 1000 characters.
- Words contain only letters and numbers after cleaning.

**File:** `16_count_words.py`

---

### Exercise 17: Filter Data from File (Challenging)
**Question:**  
Write a function `filter_data(filename, keyword)` that takes a filename and a keyword, reads a text file, and returns a list of lines containing the keyword (case-insensitive). Return lines unchanged. If an error occurs, return a dictionary with an "ERROR" key and the error message.

**Examples:**  
- File `data.txt`:
- `Temperature: 25C`
- `Humidity: 60%`
- `Temperature: 30C`
- `Pressure: 1013hPa`

- `filter_data("data.txt", "temperature")` → `["Temperature: 25C\n", "Temperature: 30C\n"]`  
- `filter_data("notfound.txt", "test")` → `{"ERROR": "File not found"}`

**Constraints:**  
- File has at most 1000 lines.
- Each line has at most 1000 characters.

**File:** `17_filter_data.py`

---

### Exercise 18: Analyze Keywords in File (Challenging)
**Question:**  
Write a function `analyze_keywords(filename, min_length, min_count)` that reads a text file and returns a dictionary of words (lowercase) with length >= `min_length` and count >= `min_count`. Ignore non-alphanumeric characters. Exclude words that are substrings of other qualifying words. Return `{"ERROR": "message"}` on error.

**Examples:**  
- File `log.txt`:
`Database error on server1
Data input failed
Database connection lost
Server1 crashed with data`

- `analyze_keywords("log.txt", 4, 2)` → `{"database": 2, "server1": 2}`  
- `analyze_keywords("notfound.txt", 3, 1)` → `{"ERROR": "File not found"}`

**Constraints:**  
- File has at most 1000 lines.
- Each line has at most 1000 characters.
- `min_length` and `min_count` are positive.

**File:** `18_analyze_keywords.py`

---

### Exercise 19: Summarize Data from CSV (Challenging)
**Question:**  
Write a function `summarize_csv(filename, column_name)` that reads a CSV file, sums the numeric values in the specified column, and returns a dictionary with `"sum"` (int if whole, else float) and `"count"`. Ignore non-numeric values. Return `{"ERROR": "message"}` on error.

**Examples:**  
- File `sales.csv`:
- `product,price,quantity
phone,299.99,5
laptop,999.5,2
cable,10,3
headset,25.75,invalid`

- `summarize_csv("sales.csv", "quantity")` returns `{"sum": 10, "count": 3}`  
- `summarize_csv("sales.csv", "price")` returns `{"sum": 1335.24, "count": 4}`  
Constraints: File has at most 1000 rows, each row has at most 1000 characters.  

**File:** `19_summarize_csv.py`

---

### Exercise 20: Calculate Region Product Profit (Comprehensive Analysis)

Write a function named `calculate_region_product_profit` that:
1. Reads a CSV file named "products.csv" with columns "product_id", "name", "category", and "unit_cost".
2. Reads a JSON file named "orders.json" containing a list of orders with fields "customer_id", "product_id", "amount", and "region".
3. Calculates the profit for each order (amount minus unit cost of the product).
4. Aggregates the profit by region and product, including all possible region-product combinations (with zero profit where no sales occurred for comprehensive analysis).
5. Writes the result to a CSV file named "region_product_profit.csv" with columns "region", "product_id", "name", and "total_profit".

**Sample Input:**
- **products.csv**:
``` product_id,name,category,unit_cost
1,Laptop,Electronics,500
2,Book,Stationery,10
3,Smartphone,Electronics,300
4,Notebook,Stationery,5
5,Headphones,Electronics,50
6,Pen,Stationery,2
7,Tablet,Electronics,400
8,Mouse,Electronics,20
9,Keyboard,Electronics,30
10,Desk Chair,Furniture,80

- **orders.json**:
```json
[
    {"customer_id": "C1", "product_id": "1", "amount": "600", "region": "North"},
    {"customer_id": "C2", "product_id": "2", "amount": "15", "region": "South"},
    {"customer_id": "C3", "product_id": "3", "amount": "350", "region": "East"},
    ...
]

**File:** `20_region_product_prifit.py`
