try:
    with (open("my_text.txt", "r", encoding="utf-8") as read_f,
          open("copy_text.txt", "w", encoding="utf-8") as write_f):
        for line in read_f:
            write_f.write(line)
        print("File copied to copy_text.txt successfully")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")

