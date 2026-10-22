def generate_numbers(limit):
    for number in range(1,limit):
        yield number
    

def numbers_divisble(numbers,divisor):
    for number in numbers:
        if number % divisor == 0:
            yield number


def square_numbers(numbers):
    for number in numbers:
        yield number ** 2
    

result = square_numbers(numbers_divisble(generate_numbers(50),5))

for nubmer in result:
    print(nubmer)