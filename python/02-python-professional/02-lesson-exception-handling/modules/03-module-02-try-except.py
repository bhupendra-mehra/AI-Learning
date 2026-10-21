# Mini Exercise

# Write a program that:

# Takes two numbers from the user.
# Divides the first by the second.
# Handles:
# ValueError
# ZeroDivisionError
# Prints the actual error message using Exception as e.
# Prints "Program Ended Successfully" after the exception handling, regardless of whether an error occurred.

try:
    number1= int(input("Enter first number : "))
    number2 = int(input("Enter second number : "))
    # print(number1/number2)
    result = number1 / number2

print(f"Result : {result}")
# except ValueError:
#     print("Invalid Number")
# except ZeroDivisionError:
#     print("Division by Zero")
# except Exception as e:
#     print(type(e))
#     print(e)
except ValueError as e:
    print("Invalid Number")
    print(e)

except ZeroDivisionError as e:
    print("Division by Zero")
    print(e)

except Exception as e:
    print(type(e))
    print(e)
    
print("Program Ended Successfully")