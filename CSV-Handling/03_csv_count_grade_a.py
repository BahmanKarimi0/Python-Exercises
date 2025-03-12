import csv

try:
    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students = list(reader)
        if students:
            grade_A_count = sum(1 for student in students if student['grade'] == 'A')
            if grade_A_count > 0:
                print(f"student{'s' if grade_A_count > 1 else ''} with grade 'A': {grade_A_count}")
            else:
                print("No student found with grade 'A'")
        else:
            print("No students found")
except FileNotFoundError:
    print("File not found")
except csv.Error:
    print("Error reading file")
except Exception as e:
    print(f"Error: {e}")
