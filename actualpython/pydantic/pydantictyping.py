from pydantic import BaseModel, ValidationError
from typing import Dict, List, Optional, Union, Dict

class Cart(BaseModel):
    user_id:int
    items: List[str]
    quantity: Optional[int] = 1
    total_price: Union[float, str]
    quantities: Dict[str, int]
    
class BlogPost(BaseModel):
    title: str
    content: str
    tags: List[str]
    
cart_data={
    "user_id":1,
    "items":["Laptop", "Smartphone"],
    "quantity":2,
    "total_price": 1499.98,
    "quantities": {"Laptop": 1, "Smartphone": 1}

}
card=Cart(**cart_data)
print(card)