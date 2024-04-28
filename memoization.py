from time import perf_counter
from functools import wraps
import sys

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

@memoize
def fibonacci(n) -> int:
    print(n)
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


start = perf_counter()
print(fibonacci(200))
end = perf_counter()

print(f"Time Taken: {end - start}")
