from functools import wraps
from time import perf_counter, sleep
import json


def cache_with_expiry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_time = perf_counter()
        cache_data = {'cache': []}

        try:
            with open('cache_data.json', 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError, IOError):
            pass

        for entry in cache_data['cache']:
            if entry['function_name'] == func.__name__ and entry['args'] == list(args) and current_time - entry[
                'timestamp'] < 30:
                print(f"From cache: {args[0]} * {args[1]}")
                return entry['result']

        result = func(*args, **kwargs)
        print(f"Calculating: {args[0]} * {args[1]}")
        cache_data['cache'].append({
            'function_name': func.__name__,
            'args': list(args),
            'result': result,
            'timestamp': current_time

        })
        try:
            with open('cache_data.json', 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, indent=4)
        except IOError:
            pass

        return result

    return wrapper


@cache_with_expiry
def multiply(a, b):
    sleep(1)
    return a * b


print(multiply(2, 3))
print(multiply(2, 3))
print(multiply(4, 5))
