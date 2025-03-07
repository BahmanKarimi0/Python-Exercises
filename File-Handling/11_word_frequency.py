import re
try:
    with (open("my_text.txt", "r", encoding="utf-8") as read_f,
          open("word_count.txt", "w", encoding="utf-8") as write_f):
        word_count = {}
        for line in read_f:
            # If dont want use re module
            # lines = line.casefold().strip().replace(",", " ")\
            #     .replace(".", " ").replace("!", " ")\
            #     .replace("?", " ").split()
            lines = re.findall(r"\w+", line.casefold())
            for word in lines:
                word_count[word] = word_count.get(word, 0) + 1
        for word, count in word_count.items():
            write_f.write(f"{word}: {count}\n")
        if word_count:
            print("File word_count.txt created successfully.")
        else:
            print("No words found in the file")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")