# ========= ATM =========

# 1.Check Balance
# 2.Deposit
# 3.Withdraw
# 4.Exit

# Choose :

# 2

# Enter Amount :
# 500

# Deposit Successful

# Current Balance : 5500

class InvalidAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class InvalidChoiceError(Exception):
    pass

class ATM:

    def __init__(self):
        self.__balance = 5000
    
    def deposit(self,amount):

        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")

        self.__balance += amount

        print("Deposit Successful")
    
    def withdraw(self,amount):

        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")
        
        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient Balance")
        
        self.__balance -= amount

        print("Withdrawal Successful")
    
    def check_balance(self):
        return self.__balance


# class Menu:

#     def options(self):
#         while True:
#             print("=============Menu============")
#             menu = ["Deposit","Withdrawal","Check Balance","Exit"]
#             option_num = 1
#             for option in menu:
#                 print(f"{option_num}.{option}")
#                 option_num += 1

#             selected_option = int(input("Select one option : "))
#             if selected_option == 1 or selected_option == 2:
#                 amount = float(input("Enter amount:"))
#                 if selected_option == 1:
#                     atm.deposit(amount)
#                 elif selected_option == 2:
#                     atm.withdrawal(amount)
#             elif selected_option == 3:
#                 atm.check_balance()
#             elif selected_option == 4:
#                 break
#             else:
#                 print("Invalid option")

class Menu:

    def __init__(self , atm):
        self.__atm = atm

    def options(self):
        while True:
            try:
                print("\n============= MENU =============")
                menu = ["Check Balance","Deposit", "Withdraw", "Exit"]

                for index, option in enumerate(menu, start=1):
                    print(f"{index}. {option}")

                selected_option = int(input("Select one option: "))

                if selected_option == 1:
                    print(f"Current Balance: {self.__atm.check_balance()}")
                elif selected_option == 2:
                    amount = float(input("Enter amount: "))
                    self.__atm.deposit(amount)
                elif selected_option == 3:
                    amount = float(input("Enter amount: "))
                    self.__atm.withdraw(amount)
                elif selected_option == 4:
                    print("Thank you for using the ATM.")
                    break
                else:
                    raise InvalidChoiceError("Invalid menu option.")

            except ValueError:
                print("Please enter a valid number.")

            except (InvalidAmountError, InsufficientBalanceError, InvalidChoiceError) as e:
                print(e)



def main():

    atm = ATM()

    menu = Menu(atm)

    menu.options()


if __name__ == "__main__":
    main()
#atm.deposit(5000)
# atm.deposit(-500)
# atm.deposit(0)
# atm.withdrawal(1000)
# print(atm.check_balance())