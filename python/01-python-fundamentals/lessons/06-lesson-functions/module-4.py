# username = input("Enter username :")
# password = input("Enter password :") // move in function will be best practice

def login(username , password):
    username = input("Enter username :")
    password = input("Enter password :")
    if username == 'admin' and password == '1234':
        return True
    return False

def calculate_discount(cart_value):
    if cart_value >= 10000:
        discount = (cart_value/100) * 20
    elif cart_value >= 5000:
        discount = (cart_value/100) * 10
    else:
        discount = 0
    return discount


def premium_discount(cart_value, premium_customer):
        premium_discount = 0
        if premium_customer:
            premium_discount = (cart_value / 100) * 5
        return premium_discount


def checkout():
    cart_value = float(input("Cart Value : "))
    premium_customer = input("Premium Customer (yes/no) : ")
    premium_customer = premium_customer.lower() == "yes"
    discount_amount = calculate_discount(cart_value)
    premium_discount_amount = premium_discount(cart_value,premium_customer)
    cart_value = cart_value - discount_amount - premium_discount_amount
    return cart_value


def show_summary(total):
    print(f"Final Amount {total}")


is_logged_in = login(username,password)

if is_logged_in:
    total = checkout()
    show_summary(total)
else:
    print("Login failed")