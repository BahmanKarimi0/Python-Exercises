from functools import wraps
import json
import datetime


def restrict_access(allowed_list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            access_stats = {
                "admin": {"granted": 0, "denied": 0},
                "editor": {"granted": 0, "denied": 0},
                "viewer": {"granted": 0, "denied": 0}
            }
            role = args[0]
            try:
                with open('access_stats.json', 'r', encoding="utf-8") as f:
                    access_stats.update(json.load(f))
            except (FileNotFoundError, json.JSONDecodeError, IOError):
                pass

            now = datetime.datetime.now().isoformat() + "Z"
            if role in allowed_list:
                result = func(*args, **kwargs)
                access_stats.setdefault(role, {"granted": 0, "denied": 0})
                access_stats[role]["granted"] += 1
                access_msg = f"[{now}] [{func.__name__}] [{role}] Access granted"
            else:
                access_stats.setdefault(role, {"granted": 0, "denied": 0})
                access_stats[role]['denied'] += 1
                access_msg = f"[{now}] [{func.__name__}] [{role}] Access denied"

            try:
                with open('access_logs.txt', 'a', encoding="utf-8") as f:
                    f.write(access_msg + "\n")
            except IOError:
                pass
            try:
                with open('access_stats.json', 'w', encoding="utf-8") as f:
                    json.dump(access_stats, f, indent=4)
            except IOError:
                pass
            if role not in allowed_list:
                raise PermissionError("Access denied: insufficient permissions")
            return result

        return wrapper

    return decorator


@restrict_access(["admin"])
def modify_data(role):
    print("Data modified successfully")


for role in ["admin", "editor", "viewer"]:
    try:
        modify_data(role)
    except PermissionError as e:
        print(f"Error for {role}: {e}")



