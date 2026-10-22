from logger import logger
from timer import timer
from exception_handler import handle_errors


@logger
@timer
@handle_errors
def divide(a, b):
    return a / b


print(divide(20, 5)) 
print(divide(20, 0))

