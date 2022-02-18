# global scope
b = 5 # global variable
def square(n): # function  scope
#    return n * n
       res = n * n # local variable
       res += 5
       return res
print(square(25))    

def mult(a, b):
    c = a * b
    return c
print(square(25))
