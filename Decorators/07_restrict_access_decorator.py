from functools import wraps
import json


def restrict_access(func):
    @wraps(func)
    def wrppaer(*args, **kwargs):
        allowed = False
        try:
            with (open('users.json', 'r', encoding='utf-8') as read_f,
                  open('access_logs.txt', 'a', encoding='utf-8') as write_f):
                users = json.load(read_f)
                for user in users:
                    if args[0] == user['username'] and user['allowed']:
                        allowed = True
                        break
                write_f.write(
                    f"{func.__name__}: {args[0]} - "
                    f"{'allowed' if args[0] == user['username'] and user['allowed'] else 'denied'}\n")

            if allowed:
                return func(*args, **kwargs)
            else:
                print(f"Access denied: user {args[0]} not allowed.")
        except (FileNotFoundError, IOError):
            pass

    return wrppaer


@restrict_access
def get_secret(user):
    print("Top secret message!")


get_secret("admin")
get_secret("guest")
get_secret("unknown")
