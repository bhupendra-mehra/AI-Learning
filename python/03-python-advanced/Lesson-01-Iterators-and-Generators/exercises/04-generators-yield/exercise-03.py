def fibonacci(limit):

    current_num, next_num  = 0 ,1
    count = 0 
    while count < limit:
        yield current_num
        current_num , next_num  = next_num , current_num + next_num
        count += 1
    
for number in fibonacci(10):
    print(number)