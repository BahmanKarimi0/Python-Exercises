try:
    with (open("my_text.txt", "r", encoding="utf-8") as read_f,
          open("long_lines.txt", "w", encoding="utf-8") as write_f):
        count = 0
        for line in read_f:
            if len(line.strip()) >= 10:
                write_f.write(line)
                count += 1
        if count > 0:
            print("File long_lines.txt created successfully")
        else:
            print("No line longer than 10 characters found")
except FileNotFoundError:
    print("File my_text.txt does not exist")
except Exception as e:
    print(f"Error: {e}")
