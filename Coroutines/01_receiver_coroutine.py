def receiver():
    while True:
        msg = yield
        print(f"Received: {msg}")


r = receiver()
next(r)
r.send("hello")
r.send("42")
r.send("world")