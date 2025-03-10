import json

try:
    with (open("people.json", "r", encoding="utf-8") as rf,
          open("graded_people.json", "w", encoding="utf-8") as wf):
        read_data = json.load(rf)
        graded_list = []
        if read_data:
            for person in read_data:
                if person["scores"]:
                    average_scores = sum(person['scores']) / len(person['scores'])
                    if average_scores >= 90:
                        grade = "A"
                    elif average_scores >= 80:
                        grade = "B"
                    elif average_scores >= 70:
                        grade = "C"
                    elif average_scores >= 60:
                        grade = "D"
                    else:
                        grade = "F"
                else:
                    grade = "N/A"
                graded_people = {key: value for key, value in person.items() if key in ["name", "age"]}
                graded_people["grade"] = grade
                graded_list.append(graded_people)
            json.dump(graded_list, wf, indent=4)
            print("File graded_people.json created successfully")
        else:
            print("No people found in people.json")
except FileNotFoundError:
    print("File not found")
except KeyError:
    print("Key 'name', 'age', or 'scores' missing")
except json.decoder.JSONDecodeError:
    print("json decode error")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Error: {e}")