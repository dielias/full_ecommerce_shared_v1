from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from shared.database import SessionLocal, engine, Base
from shared.models import Order
from pydantic import BaseModel

app = FastAPI()

# Garante que as tabelas existem
Base.metadata.create_all(bind=engine)

# Dependência para obter sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema para criar um pedido
class OrderCreate(BaseModel):
    user_id: int
    product_id: int

# 🔥 Novo schema para atualizar pedido
class OrderUpdate(BaseModel):
    user_id: int
    product_id: int

@app.post("/orders")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(user_id=order.user_id, product_id=order.product_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@app.get("/orders")
def list_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

# 🔥 Nova rota para atualizar um pedido
@app.put("/orders/{order_id}")
def update_order(order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)):
    db_order = db.get(Order, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    db_order.user_id = order_update.user_id
    db_order.product_id = order_update.product_id
    db.commit()
    db.refresh(db_order)
    return db_order

# 🔥 Nova rota para deletar um pedido
@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.get(Order, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    db.delete(db_order)
    db.commit()
    return {"message": "Pedido deletado com sucesso"}
