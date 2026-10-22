def multiplier(number):

    def multiply(value):
        return number * value
    
    return multiply

double = multiplier(2) 
triple = multiplier(3)

print(double(10)) 
print(triple(10))

# m1 = mulitplier(10)
# m2 = mulitplier(20)

# print(m1(10))
# print(m2(20))