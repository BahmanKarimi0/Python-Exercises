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

## Exercise 5: Update Age in JSON
**Question:**  
Write a Python program that reads the file `data.json` (assume it contains a dictionary with keys "name" and "age"), increases the "age" value by 1, and saves the result back to `data.json`.

**Hint:**  
Use `json.load` to read the file and `json.dump` to write back. Modify the "age" value after loading the dictionary. Open the file in "w" mode to overwrite it.

**Solution:** See `05_json_update_age.py`.

=========================================================================

## Medium Level Exercises

### Exercise 6: Calculate Average Age from JSON
**Question:**  
Write a Python program that reads the file `people.json` (assume it contains a list of dictionaries with keys "name" and "age") and calculates the average age of the people, then prints it to the console.

**Hint:**  
Use `json.load` to read the file. Calculate the average using a loop or `sum` and `len`.

**Solution:** See `06_json_average_age.py`.

=========================================================================

### Exercise 7: Filter Adults to JSON
**Question:**  
Write a Python program that reads the file `people.json` (assume it contains a list of dictionaries with keys "name" and "age"), creates a new file named `adults.json`, and saves only the people who are 18 or older. The output should be a pretty-printed JSON.

**Hint:**  
Use `json.load` to read and `json.dump` to write. Filter the list to keep only adults (age >= 18). Use `indent` in `json.dump` for pretty formatting.

**Solution:** See `07_json_adults.py`.

=========================================================================

### Exercise 8: Add Status to JSON
**Question:**  
Write a Python program that reads the file `people.json` (assume it contains a list of dictionaries with keys "name" and "age"), adds a new key "status" to each dictionary with the value "adult" if age is 18 or older, or "minor" if under 18, and saves the result back to `people.json` with pretty formatting.

**Hint:**  
Use `json.load` to read and `json.dump` to write. Use a loop or condition to set the status. Overwrite the file in "w" mode.

**Solution:** See `08_json_add_status.py`.

========================================================================

### Exercise 9: Count Adults and Minors to JSON
**Question:**  
Write a Python program that reads the file `people.json` (assume it contains a list of dictionaries with keys "name" and "age"), counts the number of adults (age >= 18) and minors (age < 18), and saves the result to a new file named `stats.json` as a dictionary with keys "adults" and "minors" in pretty-printed format.

**Hint:**  
Use `json.load` to read and `json.dump` to write. Count adults and minors using a loop or `filter`. Create a dictionary and save it.

**Solution:** See `09_json_stats.py`.

========================================================================

### Exercise 10: Create Name-Age Dictionary in JSON
**Question:**  
Write a Python program that reads the file `people.json` (assume it contains a list of dictionaries with keys "name" and "age"), creates a new dictionary with names as keys and ages as values, and saves it to a file named `name_age.json` in pretty-printed format.

**Hint:**  
Use `json.load` to read and `json.dump` to write. Build the dictionary using a loop or dictionary comprehension.

**Solution:** See `10_json_name_age.py`.

=========================================================================

## Challenging Level Exercises

### Exercise 11: Sort People by Average Score in JSON
**Question:**  
Write a Python program that reads the file `people.json` (assume it contains a list of dictionaries with keys "name", "age", and "scores" where "scores" is a list of integers), calculates the average score for each person (rounded to 2 decimal places) and adds it as a new key "average_score", sorts the people by average score in descending order, and saves the result to `sorted_people.json` in pretty-printed format.

**Hint:**  
Use `json.load` to read and `json.dump` to write. Calculate averages with `sum` and `len`, round with `round(number, 2)`, and sort with `sort` or `sorted` using a `key`.

**Solution:** See `11_json_sorted_scores.py`.

===========================================================================

### Exercise 12: Map Skills to People in JSON
**Question:**  
Write a Python program that reads the file `people.json` (assume it contains a list of dictionaries with keys "name", "age", and "skills" where "skills" is a list of strings), creates a dictionary mapping each skill to a list of names of people who have that skill, and saves it to `skills_map.json` in pretty-printed format. Ensure names are not duplicated in the lists.

**Hint:**  
Use `json.load` to read and `json.dump` to write. Use nested loops or comprehensions to build the dictionary. Use a `set` to avoid duplicate names if needed.

**Solution:** See `12_json_skills_map.py`.

============================================================================

### Exercise 13: Assign Grades to People in JSON
**Question:**  
Write a Python program that reads the file `people.json` (assume it contains a list of dictionaries with keys "name", "age", and "scores" where "scores" is a list of integers), creates a new list of dictionaries with "name", "age", and a new key "grade" based on the average score (A: ≥90, B: ≥80, C: ≥70, D: ≥60, F: <60, N/A: empty scores), and saves it to `graded_people.json` in pretty-printed format.

**Hint:**  
Use `json.load` to read and `json.dump` to write. Calculate averages with `sum` and `len`, handle empty scores separately, and use conditions to assign grades.

**Solution:** See `13_json_graded_people.py`.

============================================================================

### Exercise 14: Count Friend Mentions in JSON
**Question:**  
Write a Python program that reads the file `people.json` (assume it contains a list of dictionaries with keys "name", "age", and "friends" where "friends" is a list of strings), creates a dictionary mapping each name to the number of times it appears in others' "friends" lists, and saves it to `friend_count.json` in pretty-printed format. Include names even if they are not in the main list.

**Hint:**  
Use `json.load` to read and `json.dump` to write. Use nested loops to count mentions in "friends" lists and a dictionary to store the counts.

**Solution:** See `14_json_friend_count.py`.

===========================================================================

