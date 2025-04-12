def count_up():
    i = 1
    while True:
        yield i
        i += 1


def running_sum(gen):
    total = 0
    for number in gen:
        total += number
        yield total


counter = count_up()
sums = running_sum(counter)
for _ in range(6):
    print(next(sums))