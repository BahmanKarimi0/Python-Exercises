def sample_logs():
    yield {"message": "System started", "level": "INFO"}
    yield {"message": "Failed to connect", "level": "ERROR"}
    yield {"message": "User logged in", "level": "INFO"}


def file_logger(filename):
    level_logs = {}
    while True:
        try:
            value = yield
            while value == 'count':
                value = yield level_logs
            if isinstance(value, dict) and 'level' in value and 'message' in value:
                level_logs[value['level']] = level_logs.get(value['level'], 0) + 1
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(f"{value['level']}|{value['message']}\n")
            else:
                print(f"{value!r} is invalid")
        except GeneratorExit:
            print("file_logger coroutine closed")


l = file_logger("logs.txt")
next(l)
for log in sample_logs():
    l.send(log)
print(l.send('count'))
print(l.send('count'))
l.send({'level': 'INFO', 'message': 'Hello world'})
