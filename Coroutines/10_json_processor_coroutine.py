def json_processor(filename):
    json_dict = {}
    while True:
        try:
            value = yield
            while value == 'max':
                value = yield json_dict
            if (isinstance(value, dict) and 'id' in value and isinstance(value['id'], str)
                    and 'data' in value and isinstance(value['data'], list)
                    and all(isinstance(x, (int, float)) for x in value['data'])):
                try:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{value['id']}:{sum(value['data'])}\n")
                    json_dict[value['id']] = max(json_dict.get(value['id'], float('-inf')), sum(value['data']))
                except (FileNotFoundError, PermissionError, IOError):
                    print('Invalid dictionary')
            else:
                print('Invalid dictionary')
        except GeneratorExit:
            print('json_processor coroutine closed')
            raise


def sample_dicts():
    yield {"id": "record1", "data": [1, 2, 3]}
    yield {"id": "record2", "data": [4, 5]}
    yield {"id": "record1", "data": [10]}


p = json_processor("processed.txt")
next(p)
for d in sample_dicts():
    p.send(d)
print(p.send("max"))
