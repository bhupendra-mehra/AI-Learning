def odd_numbers(limit):
    for odd_num in range(1,limit+1,2):
        yield odd_num


for odd_number in odd_numbers(10):
    print(odd_number)