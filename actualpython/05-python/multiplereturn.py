def make_chai(name):
    return f"{name} chai"


chai=make_chai("Masala")

## paasing single argument to the function
print(chai)

def name(arg):
    pass

print(name("John"))

## return a None because we have not specified any return value in the function


def  name(arg):
    if arg=="John":
        return "Hllo john"
    else:
        return "Hello, someone else"
    
print(name("John"))
print(name("Jane"))

## function with  early return 

def multiple_args():
    return 100,20,300

a,b,c=multiple_args()

## mutiple return values from a function 
