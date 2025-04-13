def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1


def is_multiple_of_3(n):
    return n % 3 == 0


def infinite_filter(generator, condition):
    for value in generator:
        if condition(value):
            yield value


filtered = infinite_filter(natural_numbers(), is_multiple_of_3)
for _ in range(5):
    print(next(filtered))
