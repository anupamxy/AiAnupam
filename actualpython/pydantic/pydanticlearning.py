# pydantic provide data validation and settings management using python type annotations. It allows us to define data models using python classes and then validate the data against those models. It also provides a way to manage settings for our applications using environment variables or configuration files.
# Data parsing and validation
# API development
# Settings management 
# example of how to use pydantic

from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active:bool
    
input_data={"id": 1, "name": "John Doe", "email": "john.doe@example.com", "is_active": true}
user=User(**input_data)
print(user)