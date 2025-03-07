import re
try:
    with open("my_text.txt", "r", encoding="utf-8") as read_f, open("word_lengths.txt", "w", encoding="utf-8") as write_f:
        len_dic={}
        for line in read_f:
            words = set(re.findall(r"\w+", line.casefold()))
            for word in words:
                len_dic.setdefault(len(word), set()).add(word)
        if len_dic:
            print("File word_lengths.txt created successfully")
        else:
            print("No words found in my_txt.txt")
        for length, words in len_dic.items():
            write_f.write(f"{length}: {", ".join(words)}\n")
except FileNotFoundError:
    print("File my_text.txt not found")
except Exception as e:
    print(f"Error: {e}")
