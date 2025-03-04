try:
    with (open("my_text.txt", "r", encoding="utf-8") as read_f,
          open("numbered_text.txt", "w", encoding="utf-8") as write_f):
        for num_line, line in enumerate(read_f, 1):
            write_f.write(f"{num_line}: {line}")
        print("Line saved to numbered_text.txt successfully")
except FileNotFoundError:
    print("File Not Found")
except Exception as e:
    print(f"Error: {e}")
