from pydantic import BaseModel, ValidationError,computed_field,Field

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool=True
    
    @computed_field
    @property

    def discounted_price(self) -> float:
        return self.price * 0.9
    
class Bokking(BaseModel):
    product: Product
    quantity: int = Field(..., gt=0)
    
    @computed_field
    @property
    def total_price(self) -> float:
        return self.product.discounted_price * self.quantity
    
    
booking= Bokking(product=Product(id=1, name="Laptop", price=999.99), quantity=2)
print(booking.total_price)