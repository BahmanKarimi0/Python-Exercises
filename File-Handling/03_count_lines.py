try:
    with open("my_text.txt", "r", encoding="utf-8") as f:
        content = f.readlines()
        print(f"The file has {len(content)} line{'s' if len(content) > 1 else ''}")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")
