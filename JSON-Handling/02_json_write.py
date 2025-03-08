import json
info = {"name": "Sara", "city": "Tehran"}
try:
    with open("info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4)
    print("File info.json created successfully")
except Exception as e:
    print(f"Error: {e}")