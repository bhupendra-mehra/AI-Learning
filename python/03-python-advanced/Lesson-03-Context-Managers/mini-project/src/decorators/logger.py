from functools import wraps

def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"[LOG] Calling {function.__name__}")

        result = function(*args, **kwargs)

        print(f"[LOG] Completed {function.__name__}")

        return result

    return wrapper

# @logger
# def create_user():
#     print("Creating User")

# create_user()
# Output:

# [LOG] Calling create_user
# Creating User
# [LOG] Completed create_user