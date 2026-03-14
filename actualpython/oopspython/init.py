#init in a python package is a special file that is executed when the package is imported. It can be used to initialize the package, define variables, functions, or classes that should be available when the package is imported. The __init__.py file can also be used to specify which modules should be included in the package when it is imported.
class ChaiOrder:
   
   # The __init__ method is a special method in Python classes that is called when an instance of the class is created. It is used to initialize the attributes of the class with the values passed as arguments when creating an instance. In this code, the __init__ method takes two parameters, type_ and size, and assigns them to the instance variables self.type and self.size respectively.
    def __init__(self,type_,size):
        self.type=type_
        self.size=size
        
    # The summary method provides a summary of the chai order, including the type and size of the chai. It uses the instance variables self.type and self.size to generate the summary message.
        
    def summary(self):
        print(f"You have ordered a {self.size} ml cup of {self.type} chai")
        
        
order1=ChaiOrder("masala",150)
print(order1.summary())
order2=ChaiOrder("ginger",200)
print(order2.summary())