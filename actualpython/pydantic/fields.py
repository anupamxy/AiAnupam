# Field in pydantic is a way to define the type and validation rules for a specific attribute in a pydantic model. It allows you to specify the type of data that should be accepted for that attribute, as well as any additional validation rules that should be applied to ensure that the data is valid. For example, you can use a field to specify that an attribute should be a string, an integer, or a list, and you can also specify constraints such as minimum and maximum values, or regular expressions that the data must match. Fields are defined using the Field class from the pydantic library, and they are typically used in conjunction with pydantic models to create structured data representations.
# exMple of how to use field in pydantic
from pydantic import BaseModel, Field
from typing import List,Optional
class Employee(BaseModel):
    name: str = Field(...,min_length=2, max_length=100, description="The name of the employee",examples=["John Doe", "Jane Smith"])
    age: int = Field(..., gt=0,min_length=0, description="The age of the employee",examples=[25, 30, 35])
    department: Optional[str] = Field(None, description="The department of the employee")
    skills: List[str] = Field([], description="The skills of the employee")
employee=Employee(name="John Doe", age=30, department="IT", skills=["Python", "Django"])
print(employee)


class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="The username of the user", examples=["johndoe", "janedoe"])
    email: str = Field(..., regex=r'^\S+@\S+\.\S+$', description="The email address of the user", examples=["johndoe@example.com", "janedoe@example.com"])