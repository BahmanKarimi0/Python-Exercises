from functools import wraps
import json
from time import perf_counter


def rate_limit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_time = perf_counter()
        data = {'function_name': func.__name__, 'calls': 0, 'last_reset': current_time}
        try:
            with open('rate_limit.json', 'r', encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, IOError, json.JSONDecodeError):
            pass

        if current_time - data['last_reset'] > 60:
            data['calls'] = 0
            data['last_reset'] = current_time

        if data['calls'] < 3:
            data['calls'] += 1
            try:
                with open('rate_limit.json', 'w', encoding="utf-8") as f:
                    json.dump(data, f, indent=4)
            except IOError:
                pass
            return func(*args, **kwargs)
        else:
            print("Rate limit exceeded: maximum 3 calls per 60 seconds.")

    return wrapper


@rate_limit
def say_hi(user):
    print(f"Hi {user}!")


say_hi("Ali")
say_hi("Sara")
say_hi("Reza")
say_hi("Kasra")
