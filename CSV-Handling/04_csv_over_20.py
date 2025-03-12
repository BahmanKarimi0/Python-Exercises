import csv

try:
    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students = list(reader)
        if students:
            students_over_20 = list(filter(lambda x: int(x['age']) > 20, students))
            if students_over_20:
                print(f"student{'s' if len(students_over_20) > 1 else ''} over 20 years old:")
                for student in students_over_20:
                    print(student['name'])
            else:
                print("No students over 20 years old")
        else:
            print("No students found")
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid 'age' value")
except csv.Error:
    print("Invalid csv file")
except Exception as e:
    print(f"Error: {e}")
