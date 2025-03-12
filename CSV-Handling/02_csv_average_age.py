import csv

try:
    with open('students.csv', 'r', encoding='utf-8') as rf:
        reader = csv.DictReader(rf)
        students = list(reader)
        if students:
            sum_age = sum(int(student['age']) for student in students)
            average_age = sum_age / len(students)
            print(f"Average age: {round(average_age, 2)}")
        else:
            print("No students found")
except FileNotFoundError:
    print('File not found')
except ValueError:
    print('Invalid "age" value in csv file')
except csv.Error:
    print('Error reading file')
except Exception as e:
    print(f"Error: {e}")
