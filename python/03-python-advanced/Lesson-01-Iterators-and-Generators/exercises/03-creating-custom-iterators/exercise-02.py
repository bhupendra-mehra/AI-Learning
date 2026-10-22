class EvenNumbers:

    def __init__(self , limit):
        self.limit = limit
        self.current = 2
    
    def __iter__(self):
        return self
    
    def __next__(self):

        if self.current > self.limit:
            raise StopIteration    
        
        number  = self.current
        self.current += 2
        return number
    

even_nums = EvenNumbers(2)

for evn in even_nums:
    print(evn)     

