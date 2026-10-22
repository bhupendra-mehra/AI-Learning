from functools import wraps

def logger(function): 

    @wraps(function)   
    def wrapper(*args,**kwargs): 

        print("Function Started") 
    
        result = function(*args,**kwargs)
    
        print("Function Completed")

        return result
    
    return wrapper

@logger
def add(a, b): 
    return a + b

@logger
def greet(name, city="Mumbai"): 
    return f"Hello {name} from {city}"

print(add(10, 20))
print(greet("Bhupendra"))
print(greet("John", city="Delhi"))
print(add.__name__)
print(greet.__name__)