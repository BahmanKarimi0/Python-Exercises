def unique_values(lst):
    seen = set()
    for number in lst:
        if number not in seen:
            yield number
            seen.add(number)


for num in unique_values([1, 2, 2, 3, 3, 4, 1]):
    print(num)
