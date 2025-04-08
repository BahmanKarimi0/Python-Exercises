from functools import wraps
import json
import datetime
from time import sleep
from random import random


def retry_with_backoff(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        retry = {'success': 0, 'failure': 0}
        attempts = 3
        last_error = None

        try:
            with open("retry_stats.json", "r", encoding="utf-8") as f:
                retry = json.load(f)
        except (FileNotFoundError, PermissionError, json.JSONDecodeError):
            pass

        for attempt in range(1, attempts + 1):
            now = datetime.datetime.utcnow().isoformat() + "Z"
            try:
                result = func(*args, **kwargs)
                retry["success"] += 1
                retry_msg = f"[{now}] [{func.__name__}] Attempt {attempt} succeeded"
                try:
                    with open("retry_logs.txt", "a", encoding="utf-8") as f:
                        f.write(retry_msg + "\n")
                    with open("retry_stats.json", "w", encoding="utf-8") as f:
                        json.dump(retry, f, indent=4)
                except IOError:
                    pass
                return result
            except ValueError as e:
                last_error = e
                delay = 2 ** (attempt - 1)
                retry_msg = f"[{now}] [{func.__name__}] Attempt {attempt} failed with error: {str(e)}"
                if attempt < attempts:
                    retry_msg += f" - Retrying in {delay} seconds"
                else:
                    retry_msg += " - All attempts failed"
                    retry['failure'] += 1
                try:
                    with open("retry_logs.txt", "a", encoding="utf-8") as f:
                        f.write(retry_msg + "\n")
                except IOError:
                    pass
                if attempt < attempts:
                    sleep(delay)
        try:
            with open("retry_stats.json", "w", encoding="utf-8") as f:
                json.dump(retry, f, indent=4)
        except IOError:
            pass
        raise last_error
    return wrapper


@retry_with_backoff
def unstable_operation():
    if random() < 0.7:
        raise ValueError("Operation failed")
    return "Success"


unstable_operation()
