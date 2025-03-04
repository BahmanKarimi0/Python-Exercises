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
