from functools import wraps


def count_calls(func):
    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        try:
            with open("call_counts.txt", "w", encoding="utf-8") as f:
                f.write(f"Function {func.__name__} has been called {count} time{'s' if count > 1 else ''}\n")
        except IOError:
            pass
        return func(*args, **kwargs)

    return wrapper


@count_calls
def say_hello(name):
    print(f"Hello {name}!")


say_hello("Ali")
say_hello("Sara")
say_hello("Reza")
