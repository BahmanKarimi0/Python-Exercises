import json

try:
    with open('people.json', 'r', encoding="utf-8") as f:
        read_data = json.load(f)
        if read_data:
            sum_age = sum(person['age'] for person in read_data)
            average_age = sum_age / len(read_data)
            print(f"Average age: {average_age:.0f}")
        else:
            print("No people found in file")
except FileNotFoundError:
    print("File not found")
except json.decoder.JSONDecodeError:
    print("Invalid JSON")
except KeyError:
    print("Key 'age' not found")
except Exception as e:
    print(f"Error: {e}")
