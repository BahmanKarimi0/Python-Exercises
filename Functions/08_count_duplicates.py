def count_duplicates(lst: list[str]) -> dict[str, int]:
    count_word = {}
    for word in lst:
        count_word[word.casefold()] = count_word.get(word.casefold(), 0) + 1
    return count_word


print(count_duplicates(['a', 'b', 'c', 'd']))
print(count_duplicates(['apple', 'AppLe', 'banana', 'BaNana', 'Watermelon']))
