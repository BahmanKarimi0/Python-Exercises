import re
try:
    with open("my_text.txt", "r", encoding="utf-8") as read_f, open("longest_words.txt", "w", encoding="utf-8") as write_f:
        counter = 1
        for line in read_f:
            words = re.findall(r'\w+', line.casefold())
            if words:
                max_len = max(map(len, words))
                word_lst = [word for word in words if len(word) == max_len]
                write_f.write(f"Line {counter}: {', '.join(word_lst)}\n")
            else:
                write_f.write(f"Line {counter}: No words\n")
            counter += 1
        if counter > 1:
            print("File longest_words.txt created successfully")
        else:
            print("No lines found in my_text.txt")
except FileNotFoundError:
    print("File my_text.txt not found")
except Exception as e:
    print(f"Error: {e}")