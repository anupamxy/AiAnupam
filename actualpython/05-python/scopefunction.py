def name_chai(tea,milk,sugar):
    print(tea,milk,sugar)
    
    
name_chai("Darjelling","Yes","Sugar")

name_chai(tea="Green",milk="Medium",sugar="Sweet")


def special_chai(*ingredients,**extra_ingredients):
    print("Ingredients:",ingredients)
    print("Extra ingredients:",extra_ingredients)
    
    special_chai("Darjelling","Yes","Sugar",flavour="Cardamin",topping="Chocolate")
    
    # this is how we can use *args and **kwargs in a function to accept variable number of arguments and keyword arguments.
    # *args allows us to pass a variable numeber of positional arguments to a function, while **kwaegs allows us to pass a variable number of keyword arguments to a function.
    
    
def chai_order(order=[]):
    order.append("Masala chai")
    print(order)
    
chai_order()
chai_order()

# The Above code will print the same list with "Masala chai" added to it every time we call the function,because the default value of the order parameter is a mutable object a list and it is shared across  all calls to the functionn when we modify the list in one call to the function it will affeect all the call the futnion 

def chai_order(order=None):
    if order is None:
        order = []
    order.append("Masala chai")
    print(order)
    
chai_order()
chai_order()    

# In this code we have changes the defualt value of the order paramter
