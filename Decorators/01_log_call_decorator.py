from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            with open("function_logs.txt", "a", encoding="utf-8") as f:
                f.write(f"Function {func.__name__} called with args: {args}\n")
        except IOError:
            pass
        return func(*args, **kwargs)

    return wrapper


@log_call
def add_numbers(num1, num2):
    return num1 + num2


print(add_numbers(1, 2))
print(add_numbers(1, 3))
