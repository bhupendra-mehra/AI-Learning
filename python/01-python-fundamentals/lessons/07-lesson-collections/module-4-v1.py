inventory = []


def add_product():
    sku = input("Enter SKU: ")

    for product in inventory:
        if product["sku"] == sku:
            print("SKU already exists.")
            return

    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    qty = int(input("Enter Quantity: "))

    inventory.append({
        "sku": sku,
        "name": name,
        "price": price,
        "qty": qty
    })

    print("Product added successfully.")


def show_products():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n========= INVENTORY =========")

    for product in inventory:
        print(f"SKU   : {product['sku']}")
        print(f"NAME  : {product['name']}")
        print(f"PRICE : {product['price']}")
        print(f"QTY   : {product['qty']}")
        print("-----------------------------")


def search_product():
    sku = input("Enter SKU to search: ")

    for product in inventory:
        if product["sku"] == sku:
            print("\nProduct Found")
            print(f"Name  : {product['name']}")
            print(f"Price : {product['price']}")
            print(f"Qty   : {product['qty']}")
            return product

    print("Product Not Found.")
    return None


def update_quantity():
    sku = input("Enter SKU: ")
    qty = int(input("Enter New Quantity: "))

    for product in inventory:
        if product["sku"] == sku:
            product["qty"] = qty
            print("Quantity updated successfully.")
            return

    print("Product Not Found.")


def main_menu():
    while True:
        print("\n========= MENU =========")
        print("1. Add Product")
        print("2. Show Products")
        print("3. Search Product")
        print("4. Update Quantity")
        print("5. Exit")

        option = int(input("Select an option: "))

        if option == 1:
            add_product()

        elif option == 2:
            show_products()

        elif option == 3:
            search_product()

        elif option == 4:
            update_quantity()

        elif option == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid Option")


main_menu()