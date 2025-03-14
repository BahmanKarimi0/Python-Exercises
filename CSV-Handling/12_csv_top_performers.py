import csv

try:
    with (open("students.csv", "r", encoding="utf-8") as rf,
          open("top_performers.csv", "w", encoding="utf-8", newline="") as wf):
        reader = csv.DictReader(rf)
        students = list(reader)
        if students:
            for student in students:
                student['age'] = int(student['age'])
            average_age = sum(student['age'] for student in students) / len(students)
            top_performers = list(filter(lambda x: x['age'] > average_age and x['grade'] == 'A', students))
            if top_performers:
                writer = csv.DictWriter(wf, fieldnames=students[0].keys())
                writer.writeheader()
                writer.writerows(top_performers)
                print("File top_performers.csv created successfully")
            else:
                print("No students found above average age with grade 'A'")
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
