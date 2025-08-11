from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: str
    email: EmailStr

class UserResponse(BaseModel):
    user_id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
