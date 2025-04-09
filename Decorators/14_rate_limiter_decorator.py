from functools import wraps
import datetime
from time import perf_counter
import json


def rate_limiter(limit, windows):
    def decorator(func):
        call_time = []
        attempt = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            global result
            nonlocal call_time, attempt
            rate_limit_stats = {'allowed': 0, 'blocked': 0}
            rate_stats = "allowed"

            try:
                with open('rate_limit_stats.json', 'r', encoding='utf-8') as f:
                    rate_limit_stats.update(json.load(f))
            except (FileNotFoundError, json.JSONDecodeError, IOError):
                pass
            now = datetime.datetime.utcnow().isoformat() + "Z"
            current_time = perf_counter()
            call_time = [t for t in call_time if current_time - t < windows]
            print(call_time)

            if len(call_time) < limit:
                call_time.append(current_time)
                result = func(*args, **kwargs)
                rate_limit_stats['allowed'] += 1
                rate_msg = f"[{now}] [{func.__name__}] Call #{attempt + 1} within window - {rate_stats}"
                attempt += 1
            else:
                rate_limit_stats['blocked'] += 1
                rate_stats = "blocked"
                rate_msg = f"[{now}] [{func.__name__}] Call #{attempt + 1} within window - {rate_stats}"
                attempt += 1
            try:
                with open('rate_limit_logs.txt', 'a', encoding='utf-8') as f:
                    f.write(rate_msg + "\n")
            except IOError:
                pass

            try:
                with open('rate_limit_stats.json', 'w', encoding='utf-8') as f:
                    json.dump(rate_limit_stats, f, indent=4)
            except IOError:
                pass
            if attempt > 5:
                raise RuntimeError('Rate limit exceeded')
            return result

        return wrapper

    return decorator


@rate_limiter(5, 60)
def fetch_data():
    print('Data fetched successfully')


for _ in range(7):
    try:
        fetch_data()
    except RuntimeError as e:
        print(f"Error: {e}")
