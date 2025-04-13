def count_up():
    for i in range(1, 4):
        yield i


def squares():
    for i in range(1, 3):
        yield i * i


def evens():
    for i in range(2, 7, 2):
        yield i


def chained_generators(lst):
    for gen in lst:
        for num in gen:
            yield num


generators = [count_up(), squares(), evens()]
for value in chained_generators(generators):
    print(value)
