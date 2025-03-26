def most_frequent_words(text, k):
    text_list = text.split()
    word_count = {}
    for word in text_list:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_word = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    result = [word for word,count in sorted_word[:k]]
    return result


print(most_frequent_words("b b b a a a c c d d e", 2))

