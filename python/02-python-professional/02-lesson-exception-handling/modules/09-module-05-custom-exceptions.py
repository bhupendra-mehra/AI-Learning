# Mini Exercise

# Create a custom exception called:

# InvalidSalaryError

# Rules:

# Accept salary from the user.
# If salary is less than 10000, raise:
# Salary must be at least 10000.
# Otherwise print:
# Salary Accepted
# Handle the custom exception using try and except.


class InvalidSalaryError(Exception):
    pass

try:
    salary = float(input("Enter your salary :"))

    if salary < 10000:
        raise InvalidSalaryError("Salary must be at least 10000.")
except ValueError:
    print("Please enter a valid salary.") 
    
except InvalidSalaryError as e:
    print(e)

else:
    print("Salary Accepted")