from pydantic import BaseModel, ValidationError
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool=True
    
product_one=Product(id=1, name="Laptop", price=999.99,in_stock=True)
product_two=Product(id=2, name="Smartphone", price=499.99)

# Always use type annotations when defining a pydantic model. This allows pydantic to validate the data and ensure that it conforms to the expected types. In this example, we have defined a Product model with four fields: id, name, price, and in_stock. The id field is an integer, the name field is a string, the price field is a float, and the in_stock field is a boolean with a default value of True. We then create two instances of the Product model, one with all fields specified and one with only the required fields specified.
# set sensible default values for optional fields. In this example, we have set the default value of the in_stock field to True, which makes sense for a product that is available for purchase. This allows us to create instances of the Product model without having to specify the in_stock field every time.