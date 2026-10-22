class NumberIterator:

    def __init__(self,limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):

        if self.current >= self.limit:
            raise StopIteration
        
        self.current += 1

        return self.current


numbers = NumberIterator(5)

#numbers = range(5)

# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

for number in numbers:
    print(number)
