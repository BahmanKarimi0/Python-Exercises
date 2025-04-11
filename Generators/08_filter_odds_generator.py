def natural_numbers():
    i = 1
    while True:
        yield i
        i += 1


def filter_odds(gen):
    even_numbers = filter(lambda x: x % 2 == 0, gen)
    for number in even_numbers:
        yield number


natural = natural_numbers()
even = filter_odds(natural)

for _ in range(5):
    print(next(even))