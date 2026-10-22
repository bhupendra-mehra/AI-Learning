from collections import defaultdict

orders = [
  ("electronics", "Laptop"),
    ("electronics", "Mouse"),
    ("fashion", "Shirt"),
    ("electronics", "Keyboard"),
    ("fashion", "Shoes"),
    ("books", "Python Book")
]

products = defaultdict(list)

for category, product in orders:
    products[category].append(product)

print(products)

for category, product_list in products.items():
    print(f"{category}: {product_list}")
    for product in product_list:
        print(f" - {product}")