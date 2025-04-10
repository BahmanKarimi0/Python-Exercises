def squares():
    start = 1
    while True:
        yield start ** 2
        start += 1


squares_gen = squares()
for _ in range(5):
    print(next(squares_gen))