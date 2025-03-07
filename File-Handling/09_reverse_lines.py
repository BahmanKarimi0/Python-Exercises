try:
    with (open("my_text.txt", "r", encoding="utf-8") as read_f,
          open("reversed_text.txt", "w", encoding="utf-8") as write_f):
        reversed_line = read_f.readlines()
        if reversed_line:
            reversed_line.reverse()
            write_f.writelines(reversed_line)
            print("File reversed successfully")
        else:
            print("File was empty, nothing to reverse")
except FileNotFoundError:
    print("File my_text.txt not found")
except Exception as e:
    print(f"Error: {e}")