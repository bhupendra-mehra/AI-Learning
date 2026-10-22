def read_numbers(limit):
    for number in range(1,limit+1):
        yield number


def square_numbers(data):
    for number in data:
            yield number ** 2
        
result  = square_numbers(read_numbers(8))

for number in result:
    print(number)