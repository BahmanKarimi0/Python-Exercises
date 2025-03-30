from functools import wraps


def cache_result(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)

        try:
            with open('function_cache.txt', 'r', encoding='utf-8') as f:
                read = f.read()
            if str(args) not in read:
                with open('function_cache.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{args}: {cache[args]}\n")
        except (FileNotFoundError, IOError):
            with open('function_cache.txt', 'a', encoding='utf-8') as f:
                f.write(f"{args}: {cache[args]}\n")
        except PermissionError:
            return f"Permission denied."
        return cache[args]

    return wrapper


@cache_result
def multiply(x, y):
    return x * y


print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(2, 3))
