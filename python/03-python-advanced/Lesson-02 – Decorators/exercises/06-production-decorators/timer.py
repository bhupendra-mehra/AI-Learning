import time
from functools import wraps

def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        print(f"Execution Time: {end - start:.6f} seconds")

        return result

    return wrapper


# @timer
# def calculate():
#     total = sum(range(4))
#     return total

# print(calculate())