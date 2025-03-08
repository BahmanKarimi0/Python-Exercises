import json
try:
    with open("data.json", "r", encoding="utf-8") as rf, open("data_copy.json", "w", encoding="utf-8") as wf:
        for line in rf:
            print(line, file=wf)
        print("File data.json copied successfully")
except FileNotFoundError:
    print("File not found")
except json.decoder.JSONDecodeError:
    print("json decode error")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Error: {e}")

