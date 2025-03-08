import json
try:
    with open("data.json", "r", encoding="utf-8") as f:
        read_data = json.load(f)
    print("File data.json read successfully")
    print("-"*30)
    print(json.dumps(read_data, indent=4))
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")