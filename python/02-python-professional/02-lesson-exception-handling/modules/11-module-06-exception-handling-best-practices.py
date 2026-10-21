try:

    number = int(input("Enter number :"))

    result = 100 / number

except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(result)


# Questions:

# What's wrong with this code?: no instruction in input and except not have any specific exception class execpt catch all the error also not discourge and keep running code
# How would you improve it? : Imporved checked
# What happens if the user enters:
# 0 : division by zero
# abc  : invalid literal for int() with base 10: 'abc'  

#Improved One

# try:

#     number = int(input("Enter Number : "))

#     result = 100 / number

# except ValueError:
#     print("Please enter a valid integer.")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# except Exception as e:
#     print(e)

# else:
#     print(f"Result : {result}")