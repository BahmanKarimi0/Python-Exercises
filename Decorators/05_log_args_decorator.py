from functools import wraps
import csv


def log_args(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        try:
            with open('args_log.csv', 'a', encoding='utf-8', newline='') as f:
                args_log = {'Function Name': func.__name__, 'Arguments': str(args)}
                writer = csv.DictWriter(f, fieldnames=['Function Name', 'Arguments'])
                if f.tell() == 0:
                    writer.writeheader()
                writer.writerow(args_log)
        except (PermissionError, IOError):
            pass
        return value

    return wrapper


@log_args
def greet(name, string):
    return f'Hello {name}, {string}!'


print(greet("Ali", "Good morning"))
print(greet("Sara", "Hello there"))
