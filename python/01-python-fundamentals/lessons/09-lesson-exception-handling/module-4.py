# Mini Exercise

# Create a program that:

# Accepts a user's age.
# If age is less than 18, raise a ValueError with the message:
# You are not eligible to vote.
# Otherwise print:
# You are eligible to vote.
# Use try and except to handle the exception and display the message.


try:
    age = int(input("Enter your age :"))
    if age < 18:
        raise ValueError("You are not eligible to vote")
# except Exception as e:
#     print(e)
except ValueError as e:
    print(e)
else:
    print("You are eligible to vote.")