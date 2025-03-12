import json

try:
    with (open("people.json", "r", encoding="utf-8") as rf,
          open("friend_count.json", "w", encoding="utf-8") as wf):
        read_data = json.load(rf)
        friends_count = {}
        if read_data:
            for person in read_data:
                for friend in person["friends"]:
                    friends_count[friend] = friends_count.get(friend, 0) + 1
            json.dump(friends_count, wf, indent=4)
            print("File friend_count.json created successfully")
        else:
            print("No people found in people.json")
except FileNotFoundError:
    print("File people.json does not exist")
except KeyError:
    print("Key 'friends' does not exist")
except json.decoder.JSONDecodeError:
    print("json decode error")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Error: {e}")
