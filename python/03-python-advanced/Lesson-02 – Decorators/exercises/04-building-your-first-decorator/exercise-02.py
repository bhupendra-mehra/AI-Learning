def logger(function): 
    
    def wrapper(): 
        print("Before Function") 
    
        function()
    
        print("After Function") 
    
    return wrapper

@logger
def create_user():
    print("Creating User...")

@logger
def update_user():
    print("Updating User...")


@logger
def delete_user():
    print("Deleting User...")

create_user()
print("---------")
update_user()
print("---------")
delete_user()

#above line no 12 and 17 is same like below 2 lines @logger is kind of include wchih 
# which says pass welcome function as perameter into the logger function and then when you
#you welcome function indivually it also execute logger function
#decorated = logger(welcome)
#decorated()