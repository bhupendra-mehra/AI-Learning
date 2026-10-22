fruits = ("Mango","Apple","Kiwi","Grapes","Orange")

iterator = iter(fruits)

# try:
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
# except StopIteration as e:
#     print("Iterator is stopped")

try:
    while True:
        print(next(iterator))
except StopIteration:
    print("Iterator is stopped")