def count_up(start):
    while True:
        yield start
        start += 1


counter = count_up(5)
for _ in range(5):
    print(next(counter))
