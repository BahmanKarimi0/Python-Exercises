import csv

try:
    with (open("students.csv", "r", encoding="utf-8") as rf,
          open("teen_students.csv", "w", encoding="utf-8", newline="") as wf):
        reader = csv.DictReader(rf)
        students = list(reader)
        if students:
            teen_students = list(filter(lambda x: 18 <= int(x['age']) <= 20, students))
            if teen_students:
                writer = csv.DictWriter(wf, fieldnames=students[0].keys())
                writer.writeheader()
                writer.writerows(teen_students)
                print("File teen_students.csv created successfully")
            else:
                print("No students aged 18-20 found")
        else:
            print("No students found in students.csv")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("Missing 'age' key")
except ValueError:
    print("Invalid 'age' value")
except Exception as e:
    print(f"Error: {e}")
