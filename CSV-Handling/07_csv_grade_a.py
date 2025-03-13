import csv

try:
    with (open("students.csv", "r", encoding="utf-8") as rf,
          open("grade_a_students.csv", "w", encoding="utf-8",newline="") as wf):
        reader = csv.DictReader(rf)
        students = list(reader)
        if students:
            grade_a_students = list(filter(lambda x: x['grade'] == 'A', students))
            if grade_a_students:
                writer = csv.DictWriter(wf, fieldnames=students[0].keys())
                writer.writeheader()
                writer.writerows(grade_a_students)
                print("File grade_a_students.csv created successfully.")
            else:
                print("No student with grade 'A' found.")
        else:
            print("No students found in students.csv")

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("Missing 'grade' value")
except csv.Error:
    print("CSV file error")
except Exception as e:
    print(f"Error: {e}")
