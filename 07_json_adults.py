import json
try:
    with open("people.json", "r", encoding="utf-8") as rf, open("adults.json", "w", encoding="utf-8") as wf:
        read_data = json.load(rf)
        if read_data:
            adults = list(filter(lambda x: x['age'] >= 18, read_data))
            if adults:
                json.dump(adults, wf, indent=4)
                print("Adults written to adults.json")
            else:
                print("No adults found in people.json")
        else:
            print("No people found in people.json")
except FileNotFoundError:
    print("File not found")
except json.decoder.JSONDecodeError:
    print("json decode error")
except KeyError:
    print("Key 'age' not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Error: {e}")