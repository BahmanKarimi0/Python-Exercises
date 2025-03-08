import json
try:
    with open("data.json", "r", encoding="utf-8") as rf, open("data_copy.json", "w", encoding="utf-8") as wf:
        read_data = json.load(rf)
        json.dump(read_data, wf, indent=4)
        print("File data.json copied to data_copy.json successfully")
except FileNotFoundError:
    print("File not found")
except json.decoder.JSONDecodeError:
    print("json decode error")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Error: {e}")
