import csv

try:
    with (open("students.csv", "r", encoding="utf-8") as rf,
          open("grade_age_averages.csv", "w", encoding="utf-8", newline="") as wf):
        reader = csv.DictReader(rf)
        students = list(reader)
        print(students)
        grade_age_averages = {}
        if students:
            for student in students:
                grade_age_averages[student["grade"]] = grade_age_averages.setdefault(student["grade"], [])
                grade_age_averages[student["grade"]].append(int(student["age"]))
            for grade, averages in grade_age_averages.items():
                grade_age_averages[grade] = round(sum(averages) / len(averages), 2)
            writer = csv.DictWriter(wf, fieldnames=['grade', 'average_age'])
            writer.writeheader()
            writer.writerows(
                [{'grade': grade, 'average_age': averages} for grade, averages in grade_age_averages.items()])
            print("File grade_age_averages.csv created successfully.")
        else:
            print("No students found")
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
