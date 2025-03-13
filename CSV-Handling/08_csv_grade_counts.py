import csv

try:
    with (open("students.csv", "r", encoding="utf-8") as rf,
          open("grade_counts.csv", "w", encoding="utf-8", newline="") as wf):
        reader = csv.DictReader(rf)
        students = list(reader)
        if students:
            grade_counts = {}
            for student in students:
                grade_counts[student['grade']] = grade_counts.get(student['grade'], 0) + 1
            writer = csv.DictWriter(wf, fieldnames=['grade', 'count'])
            writer.writeheader()
            writer.writerows([{'grade': grade, 'count': count} for grade, count in grade_counts.items()])
            print("File grade_counts.csv created successfully")
        else:
            print("No student found in students.csv")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("Missing 'grade' key")
except Exception as e:
    print(f"Error: {e}")
