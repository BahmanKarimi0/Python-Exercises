def limited_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for num in limited_range(2, 10, 3):
    print(num)
