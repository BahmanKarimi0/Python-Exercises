import csv

try:
    with open("students.csv", "r", encoding="utf-8") as rf:
        reader = csv.DictReader(rf)
        count = 0
        for row in reader:
            count += 1
        if count > 0:
            print(f"Total students: {count}")
        else:
            print("No students in students.csv")
except FileNotFoundError:
    print("File not found")
except csv.Error:
    print("CSV Error")
except Exception as e:
    print(f"Error: {e}")
