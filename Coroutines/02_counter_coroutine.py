def counter():
    n = 0
    while True:
        try:
            value = yield
            if isinstance(value, str):
                n += 1
                print(f"Received string #{n}: {value}")
            else:
                print(f"Received non-string: {value}")
        except GeneratorExit:
            print("Counter coroutine closed")


c = counter()
next(c)
c.send("apple")
c.send("banana")
c.send("cherry")
c.send("date")