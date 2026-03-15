# Serialization and Deserialization with Pydantic
from pydantic import BaseModel,ConfigDict, ValidationError
from typing import List, Optional, Dict

import json
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

# Example user data
user_data = {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "is_active": True
}

# Create a User instance
user = User(**user_data)

# Serialize to JSON
user_json = user.json()
print(user_json)

# Deserialize from JSON
user_deserialized = User.parse_raw(user_json)
print(user_deserialized)