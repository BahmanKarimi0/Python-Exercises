import json
try:
    with open("people.json", "r", encoding="utf-8") as rf, open("name_age.json", "w", encoding="utf-8") as wf:
        read_data = json.load(rf)
        if read_data:
            name_age ={person['name']:person['age'] for person in read_data}
            json.dump(name_age,wf,indent=4)
            print("File name_age.json created successfully")
        else:
            print("No people found in people.json")
except FileNotFoundError:
    print("File not found")
except KeyError:
    print("Key 'name' or 'age' not found")
except PermissionError:
    print("Permission denied")
except json.decoder.JSONDecodeError:
    print("json decode error")
except Exception as e:
    print(f"Error: {e}")
