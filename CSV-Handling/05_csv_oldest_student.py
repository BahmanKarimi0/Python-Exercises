import csv

try:
    with open('students.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        students = list(reader)
        if students:
            oldest_student = max(students, key=lambda x: int(x['age']))
            print(f"Oldest student: {oldest_student['name']}, Age: {oldest_student['age']}")
        else:
            print("No students found")
except FileNotFoundError:
    print('File not found')
except ValueError:
    print('Invalid "age" value')
except csv.Error:
    print('Invalid csv file')
except Exception as e:
    print(f"error: {e}")
