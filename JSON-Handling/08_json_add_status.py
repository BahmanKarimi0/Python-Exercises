import json

try:
    with open("people.json", "r", encoding="utf-8") as rf:
        read_data = json.load(rf)
    if read_data:
        with open("people.json", "w", encoding="utf-8") as wf:
            [person.setdefault("status", "adult") if person['age'] >= 18 else person.setdefault("status", "minor")
                for person in read_data]
            json.dump(read_data, wf, indent=4)
            print("File people.json has been updated")
    else:
        print("No people found in people.json")
except FileNotFoundError:
    print("File not found")
except json.decoder.JSONDecodeError:
    print("json decode error")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("Key 'age' not found")
except Exception as e:
    print(f"Error: {e}")
