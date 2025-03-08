# JSON Handling Exercises
This directory contains exercises for working with JSON files in Python, divided into three levels: Simple, Medium, and Challenging.

## Exercise 1: Read JSON File
**Question:**  
Write a Python program that reads the file `data.json` (assume it contains a simple dictionary with keys "name" and "age") and prints its contents to the console.

**Hint:**  
Use the `json` module and the `load` function to read the file. Open the file with `open` and close it properly (or use `with`).

**Solution:** See `01_json_read.py`.

=========================================================================

## Exercise 2: Write JSON File
**Question:**  
Write a Python program that creates a simple dictionary with keys "name" and "city" and saves it to a file named `info.json` as JSON.

**Hint:**  
Use the `json` module and the `dump` function to write to the file. Use `with` to handle file opening and closing.

**Solution:** See `02_json_write.py`.

========================================================================

## Exercise 3: Print Name from JSON
**Question:**  
Write a Python program that reads the file `data.json` (assume it contains a dictionary with keys "name" and "age") and prints only the value of the "name" key to the console.

**Hint:**  
Use the `json` module and the `load` function to read the file. Access the "name" key after loading the dictionary.

**Solution:** See `03_json_name.py`.

==========================================================================

## Exercise 4: Copy JSON File
**Question:**  
Write a Python program that reads the file `data.json` (assume it contains a dictionary with keys "name" and "age") and creates a new file named `data_copy.json` with the same content.

**Hint:**  
Use the `json` module: `load` to read the file and `dump` to write to the new file.

**Solution:** See `04_json_copy.py`.

==========================================================================
