import re
try:
    with (open("my_text.txt", "r", encoding="utf-8") as read_f,
          open("sorted_words.txt", "w", encoding="utf-8") as write_f):
        words_dict = {}
        counter = 1
        for line in read_f:
            words = set(re.findall(r'\w+', line.casefold()))
            for word in sorted(words):
                words_dict.setdefault(word, set()).add(counter)
            counter += 1
        for words, count in sorted(words_dict.items()):
            write_f.write(f"{words}: {', '.join(map(str, sorted(count)))}\n")
        if words_dict:
            print("File sorted_words.txt created successfully.")
        else:
            print("No words found in my_text.txt.")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")
