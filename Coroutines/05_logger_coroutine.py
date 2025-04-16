def logger():
    string_list = []
    while True:
        try:
            string = yield
            if isinstance(string, str):
                string_list.append(string)
                print(f"Logged string, total: {len(string_list)}")
            else:
                print(f"{string} is not a string")
        except GeneratorExit:
            print('logger coroutine closed')


l = logger()
next(l)
l.send("error")
l.send("warning")
l.send("info")
