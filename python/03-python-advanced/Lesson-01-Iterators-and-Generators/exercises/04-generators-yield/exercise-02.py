def product_generator(products):
    for index in range(0,len(products) , 1):
        yield products[index]

products = [ "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard"]

for product in product_generator(products):
    print(product)