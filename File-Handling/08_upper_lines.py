try:
    with (open("my_text.txt", "r", encoding="utf-8") as read_f,
          open("upper_lines.txt", "w", encoding="utf-8") as write_f) :
        count = 0
        for line in read_f:
            if line.strip() and line[0].isupper():
                write_f.write(line)
                count += 1
        if count > 0:
            print("File upper_lines.txt created successfully")
except FileNotFoundError:
    print("File my_text.txt not found")
except Exception as e:
    print(f"Error: {e}")