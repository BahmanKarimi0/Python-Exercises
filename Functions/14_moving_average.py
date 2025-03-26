def moving_average(number: list[float], windows: int) -> list[float]:
    if windows > len(number):
        return []
    return [round(sum(number[i:i + windows]) / windows, 2) for i in range(len(number) - windows + 1)]


print(moving_average([1, 2, 3, 4, 5], 3))
print(moving_average([1.5, 2.5, 3.5], 2))
print(moving_average([1, 2], 1))
