def find_repeated_patterns(number: list[float], k: int) -> list[list[float]]:
    pattern_list = [number[i:i + k] for i in range(len(number) - k + 1)]
    repeated_pattern = []
    for lst in pattern_list:
        if lst not in repeated_pattern and pattern_list.count(lst) > 1:
            if sorted(lst) not in repeated_pattern:
                repeated_pattern.append(lst)
    return repeated_pattern


print(find_repeated_patterns([1, 2, 3, 1, 2, 3, 4], 3))
print(find_repeated_patterns([1.5, 2.5, 1.5, 2.5, 3.5], 2))
print(find_repeated_patterns([1, 2, 1, 2, 1, 2], 2))
print(find_repeated_patterns([1, 2, 3, 4], 2))
