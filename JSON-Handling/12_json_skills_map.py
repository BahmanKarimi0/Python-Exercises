import json

try:
    with (open("people.json", "r", encoding="utf-8") as rf,
          open("skills_map.json", "w", encoding="utf-8") as wf):
        read_data = json.load(rf)
        skills_map = {}
        if read_data:
            for person in read_data:
                for skill in person['skills']:
                    if skill not in skills_map:
                        skills_map[skill] = set()
                    skills_map[skill].add(person['name'])
            skills_map = {skill: list(names) for skill, names in skills_map.items()}
            json.dump(skills_map, wf, indent=4)
            print("File skills_map.json created successfully")
        else:
            print("No people found in people.json")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except json.decoder.JSONDecodeError:
    print("json decode error")
except KeyError:
    print("Key 'skills' not found")
except Exception as e:
    print(f"Error: {e}")