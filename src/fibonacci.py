from functools import cache
from time import perf_counter


@cache
def fibonacci(n):
    if n <= 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


t1 = perf_counter()
fibonacci(42)
t2 = perf_counter()

print(t2 - t1)

