import csv

try:
    with (open("students.csv", "r", encoding="utf-8") as rf,
          open("youngest_per_grade.csv", "w", encoding="utf-8", newline="") as wf):
        reader = csv.DictReader(rf)
        students = list(reader)
        if students:
            youngest_per_grade = {}
            for student in students:
                student['age'] = int(student['age'])
                grade = student['grade']
                if grade not in youngest_per_grade or student['age'] < youngest_per_grade[grade]['age']:
                    youngest_per_grade[grade] = student
            writer = csv.DictWriter(wf, fieldnames=students[0].keys())
            writer.writeheader()
            writer.writerows(youngest_per_grade.values())
            print("File youngest_per_grade.csv created successfully")
        else:
            print("No students found in students.csv")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("Missing 'age' or 'grade' key")
except ValueError:
    print("Invalid 'age' value")
except Exception as e:
    print(f"Error: {e}")
