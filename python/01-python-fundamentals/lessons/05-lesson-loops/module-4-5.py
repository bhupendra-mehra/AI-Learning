# Exercise 3

# Write a loop that prints numbers 1–10 but skips 5.

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)


# Exercise 4

# Write a loop that prints numbers 1–10 but stops at 7.

# for i in range(1,11):
#     if i == 7:
#         break
#     print(i)

# Exercise 5 (Final Project)

# Mini Project
# Shopping Menu

# Requirements

# ========= MENU =========

# 1. Browse Products

# 2. Checkout

# 3. Exit

# Keep showing the menu until user selects:

# 3

# When user chooses:

# 3

# Use

# break

# to exit.

# For invalid options:

# Invalid Choice

# Continue showing the menu.

# Use:

# while
# break
# if-elif-else

option = 0
while option != 3:
    print("========= MENU =========")
    print("1. Browse Products")
    print("2. Checkout")
    print("3. Exit")
    option = int(input("Select menu option : "))
    # if option == 3:
    #     break
    # elif option == 1:
    #     print("Browse Products")
    # else:
    #     print("Checkout")
    if option == 3:
        break
    elif option == 1:
        print("Browse Products")
    elif option == 2:
        print("Checkout")
    else:
        print("Invalid Choice")
