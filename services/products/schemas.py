from pydantic import BaseModel

# Esquemas Pydantic para entrada de dados
class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int

class ProductUpdate(BaseModel):
    name: str
    price: float
    quantity: int

# Esquema Pydantic para resposta, com orm_mode ativado para trabalhar direto com SQLAlchemy models
class ProductResponse(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int

    class Config:
        orm_mode = True
