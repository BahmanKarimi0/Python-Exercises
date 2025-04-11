def cycle_list(lst):
    while True:
        for i in lst:
            yield i


cycler = cycle_list([1, 2, 3])

for _ in range(10):
    print(next(cycler))