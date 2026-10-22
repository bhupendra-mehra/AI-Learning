import time
from functools import wraps

def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()
        
        try:
            return function(*args, **kwargs)

        finally:
            end = time.perf_counter()

            print(
                f"[TIMER] {function.__name__} "
                f"took {end - start:.6f} seconds"
            )

    return wrapper

# Why time.perf_counter()?

# For measuring execution duration, perf_counter() is preferred because it provides a high-resolution timer designed for performance measurements.

# @timer
# def calculate():
#     total = sum(range(4))
#     return total

# print(calculate())