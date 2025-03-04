try:
    with open("my_text.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")