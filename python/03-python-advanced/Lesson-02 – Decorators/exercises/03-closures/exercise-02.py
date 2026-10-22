def prefix(title): 
    
    def display(name): 
        print(f"{title} {name}") 
        
    return display 


mr = prefix("Mr.") 
ms = prefix("Ms.")

mr("John") 
ms("Alice")