def list_accumulator(filename):
    number = []
    while True:
        try:
            value = yield
            while value == 'average':
                yield sum(number)/len(number) if number else 0.0
            if value and isinstance(value, list) and all(isinstance(x, (int,float)) for x in value):
                try:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{','.join(str(x) for x in value)}\n")
                    number.extend(value)
                except (FileNotFoundError, IOError, PermissionError):
                    print("File error")
            else:
                print("Invalid list")
        except GeneratorExit:
            print("list_accumulator coroutine closed")


def sample_lists():
    yield [1, 2]
    yield [3]
    yield [4, 5]



a = list_accumulator('accum.txt')
next(a)
for lst in sample_lists():
    a.send(lst)
print(a.send('average'))