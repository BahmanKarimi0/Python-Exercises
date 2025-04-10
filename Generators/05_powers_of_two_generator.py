def powers_of_two():
    n = 0
    while True:
        yield 2 ** n
        n += 1


powers = powers_of_two()
for _ in range(6):
    print(next(powers))
