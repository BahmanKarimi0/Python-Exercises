def tuple_filter(filename, threshold):
    lst = []
    while True:
        try:
            item = yield
            while item == 'count':
                item = yield len(lst) if lst else 0
            if (item and len(item) == 2 and isinstance(item, tuple) and isinstance(item[0], str)
                    and isinstance(item[1], (int, float)) and item[1] >= threshold):
                try:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{item[0]}:{item[1]}\n")
                    lst.append(item[0])
                except (FileNotFoundError, PermissionError, IOError):
                    print("Invalid tuple!")
            else:
                print("Invalid tuple")
        except GeneratorExit:
            print("tuple_filter coroutine closed")


def sample_tuples():
    yield ("item1", 10.5)
    yield ("item2", 5.0)
    yield ("item3", 15.0)
    yield ("item4", 7.5)


t = tuple_filter("filtered.txt", 8.0)
next(t)
for tup in sample_tuples():
    t.send(tup)
print(t.send('count'))
