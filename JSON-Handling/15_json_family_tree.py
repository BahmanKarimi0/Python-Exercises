import json

try:
    with (open("people.json", "r", encoding="utf-8") as rf,
          open("family_tree.json", "w", encoding="utf-8") as wf):
        read_data = json.load(rf)
        if read_data:

            people = {}
            for person in read_data:
                people[person['name']] = {
                    'name': person['name'],
                    'age': person['age'],
                    'children': []
                }

            for person in read_data:
                parent = person['parent']
                if parent and parent not in people:
                    people[parent] = {
                        'name': parent,
                        'age': None,
                        'children': []
                    }

            for person in read_data:
                parent = person['parent']
                if parent:
                    people[parent]['children'].append(people[person['name']])

            roots = []
            all_names = {p['name'] for p in read_data}
            for person in read_data:
                if not person['parent'] or person['parent'] not in all_names:
                    roots.append(people[person['name']])
            for name in people:
                if name not in all_names and name:
                    roots.append(people[name])

            json.dump(roots, wf, indent=4)
            print("File family_tree.json created successfully")
        else:
            print("No people found in people.json")
except FileNotFoundError:
    print("File not found")
except KeyError:
    print("Key 'name', 'age', or 'parent' missing")
except json.decoder.JSONDecodeError:
    print("json decode error")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Error: {e}")
