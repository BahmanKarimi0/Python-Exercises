def keyval_logger(filename):
    total = 0
    while True:
        try:
            keyval = yield
            while keyval == 'total':
                keyval = yield total
            if (isinstance(keyval, dict) and ('key' in keyval and isinstance(keyval['key'], str))
                    and ('value' in keyval and isinstance(keyval['value'], (int, float)))):

                try:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{keyval['key']}={keyval['value']}\n")
                    total += keyval['value']
                except (FileNotFoundError, PermissionError, IOError):
                    print(f"File error")
            else:
                print("Invalid dictionary")
        except GeneratorExit:
            print("keyval_logger coroutine closed")


def sample_dicts():
    yield {"key": "user1", "value": 100}
    yield {"key": "user2", "value": 200}
    yield {"key": "user3", "value": 300}


k = keyval_logger('keyval.txt')
next(k)
for keyval in sample_dicts():
    k.send(keyval)

print(k.send('total'))
print(k.send('total'))
