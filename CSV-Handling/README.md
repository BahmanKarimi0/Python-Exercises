# CSV Handling Exercises

### Exercise 1: Count Students in CSV
**Question:**  
Write a Python program that reads the file `students.csv` (assume it’s a CSV file with columns "name", "age", "grade"), counts the total number of students, and prints the count to the console. Handle errors like missing files.

**Hint:**  
Use `csv.reader` or `csv.DictReader` to read the file. Loop through the rows to count students, skipping the header.

**Solution:** See `01_csv_count_students.py`.

========================================================================

### Exercise 2: Calculate Average Age in CSV
**Question:**  
Write a Python program that reads the file `students.csv` (assume it’s a CSV file with columns "name", "age", "grade"), calculates the average age of students, and prints it to the console with two decimal places. Handle errors like missing files or invalid data.

**Hint:**  
Use `csv.DictReader` to access the "age" column. Convert "age" to a number and compute the average. Check for empty data.

**Solution:** See `02_csv_average_age.py`.

========================================================================

