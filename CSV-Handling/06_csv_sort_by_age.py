import csv
try:
    with (open("students.csv", "r", encoding="utf-8") as rf,
          open("sorted_students.csv", "w", encoding="utf-8", newline="") as wf):
        reader = csv.DictReader(rf)
        students = list(reader)
        if students:
            students.sort(key=lambda x: int(x['age']))
            writer = csv.DictWriter(wf, fieldnames=students[0].keys())
            writer.writeheader()
            writer.writerows(students)
            print("File sorted_students.csv created successfully.")
        else:
            print("No students found in students.csv")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except ValueError:
    print("Invalid 'age' value")
except KeyError:
    print("Missing 'age' key")
except Exception as e:
    print(f"Error: {e}")