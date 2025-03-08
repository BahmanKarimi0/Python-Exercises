import json
try:
    with open("data.json", "r", encoding="utf-8") as f:
        read_data = json.load(f)
        print("Name extracted successfully")
        print("-"*30)
        print()
        print(f"{read_data['name']}")
except FileNotFoundError:
    print("file not found")
except json.decoder.JSONDecodeError:
    print("json decode error")
except KeyError:
    print("key 'name' not found")
except Exception as e:
    print(f"Error: {e}")