try:
    with open("my_text.txt", "r", encoding="utf-8") as f:
        words = sum(len(line.strip().split()) for line in f)
        print(f"{words} word{'s' if words > 1 else ''} in my_text.txt")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")