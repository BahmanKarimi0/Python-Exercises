import json

try:
    with open("people.json", "r", encoding="utf-8") as rf, open("sorted_people.json", "w", encoding="utf-8") as wf:
        read_data = json.load(rf)
        if read_data:
            for student in read_data:
                if student['scores']:
                    sum_scores = sum(student["scores"])
                    average_score = round(sum_scores / len(student["scores"]), 2)
                else:
                    average_score = 0
                student.setdefault('average_score', average_score)
            read_data.sort(reverse=True, key=lambda x: x['average_score'])
            json.dump(read_data, wf, indent=4)
            print("File sorted_people.json is created successfully")
        else:
            print("No students found in people.json")
except FileNotFoundError:
    print("File not found")
except KeyError:
    print("key 'scores' is missing")
except PermissionError:
    print("Permission denied")
except json.decoder.JSONDecodeError:
    print("json decode error")
except Exception as e:
    print(f"Error: {e}")
