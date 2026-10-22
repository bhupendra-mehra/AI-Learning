class OddNumberIterator:

    def __init__(self,limit):
        self.limit = limit
        self.current = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):

        if self.current > self.limit:
            raise StopIteration
        
        odd_number = self.current
        self.current += 2
        return odd_number

    
odd_nums = OddNumberIterator(8)

for odd_num in odd_nums:
    print(odd_num)
