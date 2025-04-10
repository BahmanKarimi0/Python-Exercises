from functools import wraps
import datetime
from time import sleep
import random


def retry_on_failure(max_retries, delay):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_err = None
            for attempt in range(1, max_retries + 1):
                now = datetime.datetime.utcnow().isoformat() + "Z"

                try:
                    result = func(*args, **kwargs)
                    retry_msg = f"[{now}] [{func.__name__}] Attempt #{attempt} - success"
                    try:
                        with open('retry_logs.txt', 'a', encoding='utf-8') as f:
                            f.write(retry_msg + '\n')
                    except IOError:
                        pass
                    return result
                except Exception as e:
                    last_err = e
                    retry_msg = f"[{now}] [{func.__name__}] Attempt #{attempt} - failure: {type(e).__name__}: {str(e)}"
                    try:
                        with open('retry_logs.txt', 'a', encoding='utf-8') as f:
                            f.write(retry_msg + '\n')
                    except IOError:
                        pass
                    if attempt < max_retries:
                        sleep(delay)
            raise last_err

        return wrapper

    return decorator


@retry_on_failure(max_retries=3, delay=2)
def unreliable_operation():
    number = random.randint(0, 9)
    if number > 4:
        raise ValueError("Operation failed")
    print("Operation succeeded")
    return number


unreliable_operation()
