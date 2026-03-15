from pydantic import BaseModel, ValidationError,field_validator, model_validator

class User(BaseModel):
    username: str
    email: str
    
    @field_validator('email')
    
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('Invalid email address')
        return value
    
    
class SingupData(BaseModel):
    username: str
    email: str
    password: str
    
    @model_validator(mode='before')
    def validate_password(cls, values):
        password = values.get('password')
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return values