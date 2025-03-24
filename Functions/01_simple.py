def power(base, exp):
    result = 1
    for _ in range(0, exp):
        result *= base
    return result


print(power(2, 3))
print(power(5, 0))
