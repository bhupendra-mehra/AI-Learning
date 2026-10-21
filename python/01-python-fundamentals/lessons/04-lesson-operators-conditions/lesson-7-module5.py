# Project Requirements

# The program should:

# Ask the customer's name.
# Ask the customer's age.
# Ask if they are logged in.
# Ask if the product is in stock.
# Ask the cart value.
# Calculate any discount.
# ₹10,000 or more → 20%
# ₹5,000–9,999 → 10%
# Otherwise → No discount
# Decide whether the order can be placed.
# Display the final result.
# Customer can order only if:

# Age ≥ 18
# Logged in
# Product available

#my version or project
# name = input("Enter your name:")
# age = int(input("Enter your age :"))
# username = input("Your username :")
# password = input("Your Password :")
# is_logged_in = False
# if username == 'user' and password == '1234':
#     is_logged_in = True
# if not is_logged_in:
#     print("Login please")
# else:
#     qty = int(input("Enter product qty :"))
#     is_in_stock = False
#     total = 0
#     if qty > 0:
#         is_in_stock = True
#     if not is_in_stock:
#         print("Product out of stock")
#     else:
#         cart_value = float(input("Enter cart value:"))
#         if cart_value >= 10000:
#             discount = (cart_value/100)*20
#         elif cart_value >=  5000 and cart_value <= 9999:
#             discount = (cart_value/100)*10
#         else:
#             discount = 0
#         if is_logged_in and is_in_stock and cart_value > 0:(this line not required)
#             total = float(cart_value - discount)
#         if total > 0 and age >= 18:
#             print("Place the order total ", total)
#         else:
#             print("Either total is 0 or you are minor")


#ChatGpt Version

name = input("Enter your name: ")

age = int(input("Enter your age: "))

logged_in = input("Are you logged in? (yes/no): ")

stock = input("Is the product in stock? (yes/no): ")

cart = float(input("Enter cart amount: "))

logged_in = logged_in.lower() == "yes"

stock = stock.lower() == "yes"

is_premium_customer =  input("Are you a premium customer ? (yes/no) : ")

is_premium_customer = is_premium_customer.lower() == "yes"

discount = 0
premium_discount = 0
if cart >= 10000:
    discount = cart * 0.20
elif cart >= 5000:
    discount = cart * 0.10

final_amount = cart - discount

if is_premium_customer:
    premium_discount =  (final_amount/100) * 5

final_amount = final_amount - premium_discount
if age >= 18 and logged_in and stock:
    order_allowed = True
else:
    order_allowed = False

# can be order_allowed = age >= 18 and logged_in and stock

print("\n===== ORDER SUMMARY =====")

print("Customer:", name)
print("Discount:", discount)
print("Premium Discount:", premium_discount)
print("Final Amount:", final_amount)

if order_allowed:
    print("Order Status: Approved")
else:
    print("Order Status: Rejected")