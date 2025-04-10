def even_number():
    start = 0
    while True:
        yield start
        start += 2


evens = even_number()
for _ in range(6):
    print(next(evens))