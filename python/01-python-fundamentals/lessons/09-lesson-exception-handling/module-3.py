# Mini Exercise

# Write a program that:

# Accepts two integers.
# Divides them.
# Handles:
# ValueError
# ZeroDivisionError
# Uses else to print:
# Result
# "Calculation Successful"
# Uses finally to print:Program Finished


try:
    number1 = int(input("Enter first number :"))
    number2 = int(input("Enter second number : "))
    result = number1/number2
except ValueError:
    print("Invalid numbers")
except ZeroDivisionError:
    print("Divide by zero")
except Exception as e:
    print(e)
else:
    print(f"Result : {result}")
    print("Calculation Successful")
finally:
    print("Program Finished")