import csv

try:
    with (open("students.csv", "r", encoding="utf-8") as rf,
          open("above_average_age.csv", "w", encoding="utf-8", newline="") as wf):
        reader = csv.DictReader(rf)
        students = list(reader)
        if students:
            average_age = sum(int(student['age']) for student in students) / len(students)
            above_average_age = list(filter(lambda x: int(x['age']) > average_age, students))
            if above_average_age:
                writer = csv.DictWriter(wf, fieldnames=students[0].keys())
                writer.writeheader()
                writer.writerows(above_average_age)
                print("File above_average_age.csv created successfully")
            else:
                print("No students above average age")
        else:
            print("No students found in students.csv")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("Missing 'age' key")
except ValueError:
    print("Invalid 'age' value")
except Exception as e:
    print(f"Error: {e}")
