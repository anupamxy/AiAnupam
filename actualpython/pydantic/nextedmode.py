# nested pydantic models
from pydantic import BaseModel, ValidationError
from typing import List,Optional

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    username: str
    email: str
    address: Address
    
    
Address_data={
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip_code": "12345"
}

user_data = {
    "username": "john_doe",
    "email": "john@example.com",
    "address": Address_data
}
print(user_data)