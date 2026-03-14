# static method is a method that belongs to a class rather than an instance of the class. It can be called on the class itself, without needing to create an instance. Static methods are defined using the @staticmethod decorator and do not have access to the instance (self) or class (cls) variables.
class Chai:
    @staticmethod
    def clean_ingredients(text):
        for ingredient in text.split(","):
            print(f"Cleaning {ingredient.strip()}")
raw="tea leaves, milk, sugar"
cleaned=Chai.clean_ingredients(raw)
print(cleaned)
# we can call the static method clean_ingredients using the class name Chai, without needing
