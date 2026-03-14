class Chai:
    temperature="hot"
    strength="strong"
    origin="India"
    
cutting_chai=Chai()
# we can access the class attributes using the instance of the class
print(cutting_chai.temperature)
cutting_chai.temperature="cold"
# when we assign a value to an instance attribute with the same name as a class attribute, it creates a new instance attribute that shadows the class attribute. The instance attribute takes precedence over the class attribute when accessed through the instance. Therefore, when we access cutting_chai.temperature after assigning "cold" to it, it retrieves the value from the instance attribute, which is "cold", instead of the class attribute "hot".
print(cutting_chai.temperature)
print(Chai.temperature)
del cutting_chai.temperature
# when we delete the instance attribute using del cutting_chai.temperature, it removes the instance attribute from the cutting_chai object. After deletion, when we access cutting_chai.temperature again, it falls back to the class attribute because the instance attribute has been removed. The class attribute remains unchanged, so it retrieves the value "hot" from the class attribute.
print(cutting_chai.temperature)
# this is because when we delete the instance attribute, it falls back to the class attribute. The class attribute remains unchanged, so when we access cutting_chai.temperature after deleting the instance attribute, it retrieves the value from the class attribute, which is "hot".
