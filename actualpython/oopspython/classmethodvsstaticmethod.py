# class method vs static method
class Chai:
    @staticmethod
    def boil_water():
        print("Boiling water for chai")
        
    @classmethod
    def make_chai(cls):
        cls.boil_water()
        print("Making chai using the boiled water")
        
# DIFFERENCE BETWEEN CLASS METHOD AND STATIC METHOD
# 1. A class method takes the class as the first argument, while a static method
# does not take any special first argument.
# 2. A class method can access and modify class state, while a static method cannot
# 3. A class method can be called on the class itself or on an instance of the class, while a static method can only be called on the class itself.
# 4. A class method is defined using the @classmethod decorator, while a static method is defined using the @staticmethod decorator.