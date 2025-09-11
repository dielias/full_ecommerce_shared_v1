from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int

class ProductUpdate(BaseModel):
    name: str
    price: float
    quantity: int

class ProductResponse(BaseModel):
    product_id: int   # <-- bate com o models
    name: str
    price: float
    quantity: int

    class Config:
        orm_mode = True
