import csv

try:
    with (open("students.csv", "r", encoding="utf-8") as rf,
          open("above_grade_average.csv", "w", encoding="utf-8", newline="") as wf):
        reader = csv.DictReader(rf)
        students = list(reader)
        if students:
            for student in students:
                student['age'] = int(student['age'])
            grade_sums = {}
            grade_counts = {}
            for student in students:
                grade = student['grade']
                grade_sums[grade] = grade_sums.get(grade, 0) + student['age']
                grade_counts[grade] = grade_counts.get(grade, 0) + 1
            grade_averages = {grade: grade_sums[grade] / grade_counts[grade]
                              for grade in grade_sums}

            above_grade_average = list(filter(lambda x: x['age'] > grade_averages[x['grade']], students))
            if above_grade_average:
                writer = csv.DictWriter(wf, fieldnames=students[0].keys())
                writer.writeheader()
                writer.writerows(above_grade_average)
                print("File above_grade_average.csv created successfully")
            else:
                print("No students found above their grade's average age")
        
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
