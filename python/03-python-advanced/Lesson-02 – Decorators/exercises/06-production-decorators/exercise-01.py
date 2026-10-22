def outer(choice):

    def welcome():
        print("Welcome to the app")

    def goodbye():
        print("Goodbye from the app")

    if choice == "welcome":
        return welcome
    elif choice == "goodbye":
        return goodbye
    else:
        raise ValueError("Invalid choice")


task = outer("welcome")
task()

task = outer("goodbye")
task()

task = outer("test")
task()
