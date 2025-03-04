try:
    with (open("my_text.txt", "r", encoding="utf-8") as read_f,
          open("new_text.txt", "w", encoding="utf-8") as write_f):
        for line in read_f:
            write_f.write(line.replace('hello','goodbye'))
        print("text has been replaced and saved to new_text.txt")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"Error: {e}")
