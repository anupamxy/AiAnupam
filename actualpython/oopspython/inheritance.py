# inheritance in python



class Chai:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
    def prepare(self):
        print(f"Preparing a {self.size} ml cup of {self.type} chai")
        
 # The MasalaChai class inherits from the Chai class, which means that it has access to all the methods and attributes of the Chai class. In addition to that, it also has its own method add_spices, which is specific to the MasalaChai class. This allows us to create a new class that is a specialized version of the Chai class, without having to duplicate the code in the Chai class.       
class MasalaChai(Chai):
    def add_spices(self):
        print("Adding spices to the chai")
        
        
# this is the example of composition where we are using the Chai class inside the ChaiShop class to create a chai object and call its prepare method. This allows us to reuse the code in the Chai class and avoid duplication.
class ChaiShop:
    chai_cls=Chai
    def __init__(self):
        self.chai=self.chai_cls("masala",150)
    def prepare_chai(self):
        print("Welcome to the chai shop!")
        self.chai.prepare()
        

shop=ChaiShop()
shop.prepare_chai()
class Fancyshop(ChaiShop):
    chai_cls=MasalaChai