from functools import wraps

def handle_errors(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        try:
            return function(*args, **kwargs)

        except Exception as error:
            print(f"Error: {error}")
            raise

    return wrapper

# @handle_errors
# def divide(a, b):
#     return a / b


# print(f"Divide Result : {divide(19893,83)}")