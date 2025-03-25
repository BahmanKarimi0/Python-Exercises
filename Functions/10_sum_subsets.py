def sum_subsets(lst: list[int], target: int) -> bool:
    if target < 0 or (len(lst) == 0 and target != 0):
        return False
    if target == 0:
        return True
    dp = [False] * (target + 1)
    dp[0] = True
    for num in lst:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
    return dp[target]


print(sum_subsets([], 1))
print(sum_subsets([1, 2, 3, 4, 5], 16))
print(sum_subsets([1, 2, 3, 4, 8, 6, 4, 3, 0, 8, 6, 4, 2, 4, 1, 34], 167))
print(sum_subsets([2, 4, 6, 9, 4], 8))
