from functools import wraps
import datetime
import json


def advanced_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        try:
            with open("log_stats.json", "r", encoding="utf-8") as f:
                logger = json.load(f)
        except (FileNotFoundError, PermissionError, IOError, json.JSONDecodeError):
            pass
        now = datetime.datetime.utcnow().isoformat() + "Z"

        try:
            result = func(*args, **kwargs)
            if result >= 10:
                logger['WARNING'] += 1
                log_msg = f"[WARNING] {now} [{func.__name__}] Result exceeds 10: {round(result, 2)}\n"
            else:
                logger['INFO'] += 1
                log_msg = f"[INFO] {now} [{func.__name__}] Function executed successfully\n"

        except Exception as e:
            logger['ERROR'] += 1
            log_msg = f"[ERROR] {now} [{func.__name__}] {str(e)}"

            try:
                with open("app_logs.txt", "a", encoding="utf-8", newline="") as f:
                    f.write(log_msg + "\n")
            except (FileNotFoundError, PermissionError, IOError):
                pass
            try:
                with open("log_stats.json", "w") as f:
                    json.dump(logger, f, indent=4)
            except (FileNotFoundError, PermissionError, IOError):
                pass
            raise e
        try:
            with open("app_logs.txt", "a", encoding='utf-8', newline="") as f:
                f.write(log_msg + "\n")
        except IOError:
            pass
        try:
            with open("log_stats.json", "w", encoding='utf-8') as f:
                json.dump(logger, f, indent=4)
        except IOError:
            pass
        return result

    return wrapper


@advanced_logger
def divide_numbers(a, b):
    return a / b


divide_numbers(20, 2)
divide_numbers(5, 2)
divide_numbers(10, 0)
