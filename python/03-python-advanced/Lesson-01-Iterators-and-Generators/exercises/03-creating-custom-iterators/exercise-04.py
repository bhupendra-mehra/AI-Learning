class ProductIterator:

    def __init__(self,products):
        self.products = products
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= len(self.products):
            raise StopIteration

        position = self.current

        self.current += 1

        return self.products[position]

products = [ "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard" ]

iterator = ProductIterator(products) 

for product in iterator: 
    print(product)