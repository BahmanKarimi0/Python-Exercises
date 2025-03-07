import re

try:
    with open("my_text.txt", "r", encoding="utf-8") as read_f, open("word_pairs.txt", "w", encoding="utf-8") as write_f:
        pair_dict = {}
        for line in read_f:
            words = re.findall(r'\w+', line.casefold())
            for i in range(len(words) - 1):
                pair = words[i] + "-" + words[i + 1]
                pair_dict[pair] = pair_dict.get(pair, 0) + 1
        for pair, count in pair_dict.items():
            if count > 1:
                write_f.write(f"{pair}: {count}\n")
        if pair_dict:
            print("File word_pair.txt created successfully")
        else:
            print("No pair words found in my_text.txt")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")
