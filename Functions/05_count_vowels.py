vowels = ("a", "e", "i", "o", "u")


def count_vowels(s):
    count = 0
    for i in s.casefold():
        if i in vowels:
            count += 1
    return count


print(count_vowels("Hello"))
print(count_vowels("PytHons PrOgrAmer"))
