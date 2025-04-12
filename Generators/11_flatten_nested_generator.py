def flatten_nested(lst):
    for i in lst:
        if isinstance(i, list):
            yield from flatten_nested(i)
        else:
            yield i


for num in flatten_nested([1, [2, [3, 4], 5], [6]]):
    print(num)
