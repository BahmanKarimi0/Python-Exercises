import json

try:
    with open("people.json", "r", encoding="utf-8") as rf, open("stats.json", "w", encoding="utf-8") as wf:
        read_data = json.load(rf)
        if read_data:
            stats = {}
            for person in read_data:
                if person['age'] >= 18:
                    stats['adults'] = stats.get('adults', 0) + 1
                else:
                    stats['minor'] = stats.get('minor', 0) + 1
            json.dump(stats, wf, indent=4)
            print("File stats.json created successfully")
        else:
            print("No people found in people.json")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("Key 'age' not found")
except json.decoder.JSONDecodeError:
    print("json decode error")
except Exception as e:
    print(f"Error: {e}")
