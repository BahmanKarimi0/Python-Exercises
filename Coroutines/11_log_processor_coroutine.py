import json


def log_reader(filename):
    try:
        with (open(filename, 'r', encoding='utf-8') as f):
            for line in f:
                try:
                    reader = json.loads(line.strip())
                    if (isinstance(reader, dict) and 'event' in reader and isinstance(reader['event'], str)
                            and 'level' in reader and isinstance(reader['level'], str) and 'value' in reader
                            and isinstance(reader['value'], (float, int))):
                        yield reader
                    else:
                        print('Invalid log')
                except json.decoder.JSONDecodeError:
                    print('Invalid log')
    except (FileNotFoundError, PermissionError, IOError):
        print('File error')
    finally:
        print('log_reader coroutine closed')


def log_filter(level):
    while True:
        try:
            item = yield
            if item['level'] == level:
                yield item
            else:
                print('Invalid log')
        except GeneratorExit:
            print('log_filter coroutine closed')
            raise


def log_writer(txt_file):
    count = 0
    while True:
        try:
            item = yield
            while item == 'count':
                item = yield count
            try:
                with open(txt_file, 'a', encoding='utf-8') as f:
                    f.write(f"{item['event']}:{item['value']}\n")
                count += 1
            except (FileNotFoundError, json.decoder.JSONDecodeError, PermissionError, IOError):
                print('File error')

        except GeneratorExit:
            print('log_writer coroutine closed')
            raise


r = log_reader("logs.txt")
f = log_filter("ERROR")
w = log_writer("errors.txt")
next(w)
next(f)
next(r)
for item in r:
    filtered_item = f.send(item)
    if filtered_item:
        w.send(filtered_item)
print(w.send("count"))
