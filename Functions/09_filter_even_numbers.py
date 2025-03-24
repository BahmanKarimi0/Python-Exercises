def filter_even_numbers(lst: list[int]) -> list[int]:
    return [num for num in lst if num & 1 == 0]


print(filter_even_numbers([1, 2, 3, -4, 5]))
