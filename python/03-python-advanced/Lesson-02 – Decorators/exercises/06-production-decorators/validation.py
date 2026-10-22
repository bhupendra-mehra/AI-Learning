from functools import wraps

def positive_numbers(function):

    @wraps(function)
    def wrapper(number):

        if number <= 0:
            raise ValueError("Number must be positive")

        return function(number)

    return wrapper


# @positive_numbers
# def square(number):
#     return number ** 2

# print(f"Square of Number : {square(-9)}")