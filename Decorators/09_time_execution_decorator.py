from functools import wraps
from time import sleep, perf_counter, time
import csv


def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = func(*args, **kwargs)
        end = perf_counter() - start
        print(f"Execution time: {round(end, 3)} seconds")
        if end > 1:
            print("Warning: execution took longer than 1 second!")

        try:
            with open('execution_times.csv', 'a', encoding='utf-8', newline="") as f:
                writer = csv.DictWriter(f, fieldnames=['Function Name', 'Execution Time', 'Timestamp'])
                if f.tell() == 0:
                    writer.writeheader()
                writer.writerow({'Function Name': func.__name__, 'Execution Time': round(end, 3), 'Timestamp': time()})
        except IOError:
            pass
        return value

    return wrapper


@time_execution
def slow_add(a, b):
    sleep(1.5)
    return a + b


slow_add(5, 3)
slow_add(2, 4)
