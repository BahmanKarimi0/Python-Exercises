# File Handling Exercises

## Exercise 1: Writing to a Text File
**Question:**  
Write a Python program that takes a text input from the user (using `input`) and saves it to a file named `my_text.txt`. If the file already exists, the new text should be appended to the end of the file (not overwrite it).

**Hint:** Use `open()` with the `'a'` (append) mode.

**Solution:** See `01_write_to_file.py`.

===========================================================================================

## Exercise 2: Reading the Whole File
**Question:**  
Write a Python program that reads the entire content of the file `my_text.txt` and prints it to the console as a single string.

**Hint:**  
Use `open()` with the `'r'` (read) mode and the `read()` method.

**Solution:** See `02_read_file.py`.

==========================================================================================

## Exercise 3: Counting Lines
**Question:**  
Write a Python program that counts the number of lines in the file `my_text.txt` and prints the count to the console.

**Hint:**  
You can read the file line by line and count them, or use a method like `readlines()`.

**Solution:** See `03_count_lines.py`.

========================================================================================

## Exercise 4: Copying a File
**Question:**  
Write a Python program that reads the content of the file `my_text.txt` and copies it into a new file named `copy_text.txt`.

**Hint:**  
Read the first file and write its content to the second file. You can use `read()` or process it line by line.

**Solution:** See `04_copy_file.py`.

========================================================================================

## Exercise 5: Numbered Lines
**Question:**  
Write a Python program that reads the file `my_text.txt` and saves each line with its line number into a new file named `numbered_text.txt` (e.g., "1: Hello").

**Hint:**  
Use a loop to read lines and add the line number to each one.

**Solution:** See `05_numbered_lines.py`.

========================================================================================

## Exercise 6: Counting Words
**Question:**  
Write a Python program that reads the file `my_text.txt` and counts the number of words in it, then prints the result to the console. Assume words are separated by spaces.

**Hint:**  
You can read the file line by line and use the `split()` method to separate words.

**Solution:** See `06_count_words.py`.

========================================================================================

## Exercise 7: Replacing a Word
**Question:**  
Write a Python program that finds a specific word (e.g., "hello") in the file `my_text.txt` and replaces it with another word (e.g., "goodbye"), then saves the result to a new file named `new_text.txt`.

**Hint:**  
You can read the file line by line and use the `replace()` method for substitution.

**Solution:** See `07_replace_word.py`.

========================================================================================

## Exercise 8: Uppercase Starting Lines
**Question:**  
Write a Python program that reads the file `my_text.txt` and saves the lines that start with an uppercase letter into a new file named `upper_lines.txt`.

**Hint:**  
You can use methods like `isupper()` or check the first character of each line, and only write the lines that meet the condition.

**Solution:** See `08_upper_lines.py`.

========================================================================================

## Exercise 9: Reversing Lines
**Question:**  
Write a Python program that reads the file `my_text.txt`, reverses the order of its lines (from last to first), and saves the result into a new file named `reversed_text.txt`.

**Hint:**  
You can read all lines into a list and reverse them, or use a method like `reversed()`.

**Solution:** See `09_reverse_lines.py`.

========================================================================================

## Exercise 10: Long Lines
**Question:**  
Write a Python program that reads the file `my_text.txt` and saves only the lines with more than 10 characters into a new file named `long_lines.txt`.

**Hint:**  
You can check the length of each line with `len()` and filter lines longer than 10 characters.

**Solution:** See `10_long_lines.py`.

========================================================================================

## Exercise 11: Word Frequency
**Question:**  
Write a Python program that reads the file `my_text.txt` and creates a dictionary where the keys are unique words and the values are their frequency of occurrence. Save this dictionary to a new file named `word_count.txt`, with each line formatted as "word: count" (e.g., "hello: 3").

**Hint:**  
You can split words with `split()` and use a dictionary to count them. Handle spaces, empty lines, and punctuation (like commas and periods).

**Solution:** See `11_word_frequency.py`.

===========================================================================================

## Exercise 12: Word Lengths
**Question:**  
Write a Python program that reads the file `my_text.txt` and categorizes words based on their length. Save the result to a new file named `word_lengths.txt`, with each line formatted as "length: word1, word2, ..." (e.g., "3: the, cat"). Ensure duplicate words are only listed once.

**Hint:**  
You can use a dictionary where keys are word lengths and values are sets of words with that length. Handle punctuation and spaces.

**Solution:** See `12_word_lengths.py`.

==========================================================================================

## Exercise 13: Sorted Words with Line Numbers
**Question:**  
Write a Python program that reads the file `my_text.txt` and sorts its words alphabetically. Save the result to a new file named `sorted_words.txt`, with each line formatted as "word: line_number1, line_number2, ..." (e.g., "hello: 1, 3"), where line numbers indicate the lines in the original file where the word appears. If a word appears in multiple lines, list all line numbers separated by commas.

**Hint:**  
You can use a dictionary where keys are words and values are sets of line numbers. Handle punctuation and spaces.

**Solution:** See `13_sorted_words.py`.

==========================================================================================
