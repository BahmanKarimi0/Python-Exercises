import re


def reverse_words(text: str) -> str:
    word_list = re.findall(r'\w+', text)
    new_text = []
    for word in range(len(word_list) - 1, -1, -1):
        new_text.append(word_list[word])
    return ' '.join(new_text)


print(reverse_words('Hello World'))
print(reverse_words('This is a test txt'))
