from pydantic import BaseModel, Field

from basic.schema import BaseSchema

class CreateUserSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str = Field(..., min_length=6, max_length=72, description="Password must be 6 to 72 characters long")
    phone_number: str = Field(min_length=13, max_length=13)
    class Config:
        from_attributes = True  # Updated from orm_mode

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class UserResponseSchema(BaseSchema):
    username: str
    first_name: str
    last_name: str
    class Config:
        from_attributes = True  # Updated from orm_mode

class UserLoginSchema(BaseModel):
    username: str
    password: str

class UserVerifications(BaseModel):
    password: str
    new_password: str = Field(min_length=6, max_length=72, description="New password must be 6 to 72 characters long")