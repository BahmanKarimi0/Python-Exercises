def accumulator():
    sum_number = 0
    while True:
        try:
            number = yield
            if isinstance(number, (int, float)):
                sum_number += number
                print(f"Current sum: {sum_number}")
            else:
                print("Send invalid number")
        except GeneratorExit:
            print("Accumulator coroutine closed")


a = accumulator()
next(a)
a.send(10)
a.send(20.5)
a.send(30)
a.send(40.75)
