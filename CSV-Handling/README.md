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

### Exercise 3: Count Students with Grade A in CSV
**Question:**  
Write a Python program that reads the file `students.csv` (assume it’s a CSV file with columns "name", "age", "grade"), finds the number of students with grade "A", and prints the count to the console. Handle errors like missing files or invalid data.

**Hint:**  
Use `csv.DictReader` to access the "grade" column. Loop through or use a condition to count students with "A". Check for no matches.

**Solution:** See `03_csv_count_grade_a.py`.

=======================================================================

### Exercise 4: Find Students Over 20 in CSV
**Question:**  
Write a Python program that reads the file `students.csv` (assume it’s a CSV file with columns "name", "age", "grade"), finds the names of students whose age is over 20, and prints each name on a new line to the console. Handle errors like missing files or invalid data.

**Hint:**  
Use `csv.DictReader` to access "name" and "age". Convert "age" to a number and filter based on the condition. Check for no matches.

**Solution:** See `04_csv_over_20.py`.

=======================================================================

### Exercise 5: Find Oldest Student in CSV
**Question:**  
Write a Python program that reads the file `students.csv` (assume it’s a CSV file with columns "name", "age", "grade"), finds the student with the highest age, and prints their name and age to the console. Handle errors like missing files or invalid data.

**Hint:**  
Use `csv.DictReader` to access "name" and "age". Convert "age" to a number and find the maximum using `max()` or a loop. Check for empty data.

**Solution:** See `05_csv_oldest_student.py`.

======================================================================

### Exercise 6: Sort Students by Age in CSV
**Question:**  
Write a Python program that reads the file `students.csv` (assume it’s a CSV file with columns "name", "age", "grade"), sorts the students by age (ascending), and saves the sorted data to a new file `sorted_students.csv`. Handle errors like missing files or invalid data.

**Hint:**  
Use `csv.DictReader` to read and `csv.DictWriter` to write. Convert "age" to a number and sort with `sorted()`. Check for empty data.

**Solution:** See `06_csv_sort_by_age.py`.

======================================================================
