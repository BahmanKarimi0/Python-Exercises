import json

try:
    with open("data.json", "r", encoding="utf-8") as rf:
        read_data = json.load(rf)
        read_data['age'] += 1
    with open("data.json", "w", encoding="utf-8") as wf:
        json.dump(read_data, wf, indent=4)
        print("File successfully updated")
except FileNotFoundError:
    print("File not found")
except json.decoder.JSONDecodeError:
    print("Json decode error")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("key 'age' not found")
except Exception as e:
    print(f"Error: {e}")
