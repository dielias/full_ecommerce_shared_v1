from pydantic import BaseModel
from typing import List

class ProductQuantity(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    user_id: int
    products: List[ProductQuantity]

class OrderUpdate(BaseModel):
    user_id: int
    products: List[ProductQuantity]

class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    products: List[ProductQuantity]

    class Config:
        orm_mode = True
