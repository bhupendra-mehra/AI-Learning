# products = ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard"]

# products = (product for product in products)

# for product in products:
#     if len(product) > 6:
#         print(product)

products = (
    product
    for product in products
    if len(product) > 6
)

for product in products:
    print(product)
