list_numbers = [x for x in range(1,21)]

#Stores all values at once in the memory.

for number in list_numbers:
    print(number)



gen_numbers = (x for x in range(1,21))

#Generates one value at a time.

for number in gen_numbers:
    print(number)
