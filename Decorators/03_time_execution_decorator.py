from functools import wraps
import time


def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        try:
            with open("execution_times.txt", "a", encoding="utf-8") as f:
                f.write(
                    f"Function {func.__name__} took approximately "
                    f"{total_time:.1f} second{'s' if total_time !=1 else ''}\n")
        except IOError:
            pass
        return value

    return wrapper


@time_execution
def slow_sum(a, b):
    time.sleep(1)
    return a + b


print(slow_sum(1, 2))
