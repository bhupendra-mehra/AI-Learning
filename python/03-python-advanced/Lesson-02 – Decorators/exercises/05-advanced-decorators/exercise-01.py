def display(*args): 
    print(args) 

display(10, 20, 30)


def display(**kwargs): 
    print(kwargs) 

display(name="John", age=25)