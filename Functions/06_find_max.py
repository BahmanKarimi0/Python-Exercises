def find_max(lst: list["int"]) -> int:
    max_val = float("-inf")
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


print(find_max([1, 2, 3]))
print(find_max([18, 56, 21, 7, 9, 45, 2, 3]))
