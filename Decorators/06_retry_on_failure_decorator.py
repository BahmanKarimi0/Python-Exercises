from functools import wraps
from random import uniform
from time import sleep


def retry_on_failure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for attempt in range(1, 4):
            try:
                value = func(*args, **kwargs)
                return value
            except Exception as e:
                with open('retry_logs.txt', 'a', encoding='utf-8') as f:
                    f.write(f'Attempt {attempt} for {func.__name__} failed: {e}\n')
                if attempt < 3:
                    sleep(uniform(0.5, 1.5))
                else:
                    raise e

    return wrapper


@retry_on_failure
def divide(x, y):
    return x / y


print(divide(10, 2))
print(divide(5, 0))

