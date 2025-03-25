def limited_factorial(n: int, limit: int) -> int:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    if factorial > limit:
        return limit
    return factorial


print(limited_factorial(4, 14))
