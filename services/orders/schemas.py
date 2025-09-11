from pydantic import BaseModel

class OrderCreate(BaseModel):
    user_id: int
    product_id: int  # apenas um produto

class OrderUpdate(BaseModel):
    user_id: int
    product_id: int  # apenas um produto

class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    product_id: int  # apenas um produto

    class Config:
        orm_mode = True

