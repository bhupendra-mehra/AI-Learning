inventory  = []
is_show_menu = True
def add_product():
    sku = input("Enter Sku :")
    for product in inventory:
        if product["sku"] == sku:
            print("SKU already exist")
            return

    product_name = input("Enter Product name : ")
    price = float(input("Enter Price : "))
    qty = int(input("Enter Quantity :"))
    product =  {
        'sku': sku,
        'name' : product_name,
        'price' : price,
        "qty" : qty
    }
    # return inventory.append(product) if add retrun here then append() always returns None insated updated below. 
    inventory.append(product)
    print("Product added successfully.")
    # or return True This is standard practice

def show_products():
    if not inventory:
        print("Inventory empty")
        return
    print("========= INVENTORY =========")
    for product in inventory :
        #for key,value in product.items(): #not required
            # print(f"{key.upper()} : {value}") instead of this use below because product can have many element or keys but we need specific ones only
        print(f"SKU   : {product['sku']}")
        print(f"NAME  : {product['name']}")
        print(f"PRICE : {product['price']}")
        print(f"QTY   : {product['qty']}")
    print("-----------------------------")  


def search_product():
    sku = input("Enter sku to search : ")
    #is_product_found = False not required
    # for product in inventory :
    #     for key , value in product.items(): Instead of
    #if(key == "sku" and value == sku):
    #Use
    for product in inventory :
        if product["sku"] == sku:
            print("Product Found")
            print(product.get("name"))
            print(product.get("price"))
            print(product.get("qty"))
            return product
            break
    # if not is_product_found:
    #     print("Product Not Found")
    #     return False
    print("Product Not Found")
    return None
               
    

def update_quantity():
    sku = input("Enter sku to update quanity : ")
    qty = int(input("Enter quantity :"))
    # for product in inventory :
    #     for key , value in product.items():
    #         if(key == "sku" and value == sku): same issue as search
    for product in inventory :
        if product["sku"] == sku:
            product['qty'] = qty
            break


def main_menu():
    print("========= MENU =========")
    print("1. Add Product")
    print("2. Show Products")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Exit")
    return int(input("Select any one option : "))

while is_show_menu:
    selected_option = main_menu()
    if selected_option == 1:
        add_product()
    elif selected_option == 2:
        show_products()
    elif selected_option == 3:
        search_product()
    elif selected_option == 4:
         update_quantity()
    # else:
    #     is_show_menu = False instead of this use because This means 7 10 99 also exits
    elif selected_option == 5:
        is_show_menu = False
    else:
        print("Invalid Option")

            


