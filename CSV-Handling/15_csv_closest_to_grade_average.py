import csv

try:
    with open("students.csv", "r", encoding="utf-8") as rf, open("closest_to_grade_average.csv", "w", encoding="utf-8",
                                                                 newline="") as wf:
        reader = csv.DictReader(rf)
        students = list(reader)

        if students:
            grade_sum = {}
            grade_count = {}
            for student in students:
                student['age'] = int(student['age'])
                grade = student['grade']
                grade_sum[grade] = grade_sum.get(grade, 0) + student['age']
                grade_count[grade] = grade_count.get(grade, 0) + 1
            average_grade_age = {grade: grade_sum[grade] / grade_count[grade] for grade in grade_sum}

            closest_to_grade_average = {}
            for student in students:
                grade = student['grade']
                if grade not in closest_to_grade_average or abs(average_grade_age[grade] - student['age']) < abs(
                        average_grade_age[grade] - closest_to_grade_average[grade]['age']):
                    closest_to_grade_average[grade] = student

            writer = csv.DictWriter(wf, fieldnames=students[0].keys())
            writer.writeheader()
            writer.writerows(closest_to_grade_average.values())
            print("File closest_to_grade_average.csv created successfully")
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
