# numbers = (x for x in range(1,100))

# for number in numbers:
#     if (number%3 == 0 and number%5 == 0):
#         print(number)

numbers = (
    x
    for x in range(1, 101)
    if x % 3 == 0 and x % 5 == 0
)

for number in numbers:
    print(number)   