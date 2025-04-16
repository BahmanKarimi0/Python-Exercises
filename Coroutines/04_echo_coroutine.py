def echo():
    value = None
    while True:
        try:
            value = yield value
        except GeneratorExit:
            print('echo coroutine closed')


e = echo()
next(e)
print(e.send("test"))
print(e.send(100))
print(e.send(3.14))
