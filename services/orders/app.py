from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List

from services.shared.database import SessionLocal, engine
from services.shared.models import Base, Order
from services.orders.schemas import OrderCreate, OrderUpdate, OrderResponse, ProductQuantity

app = FastAPI()

# Cria as tabelas (se ainda não existirem)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/orders", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    products_json = [p.dict() for p in order.products]
    db_order = Order(user_id=order.user_id, products=products_json)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return OrderResponse(
        order_id=db_order.id,
        user_id=db_order.user_id,
        products=db_order.products
    )

@app.get("/orders", response_model=List[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    stmt = select(Order)
    orders = db.execute(stmt).scalars().all()
    return [
        OrderResponse(
            order_id=o.id,
            user_id=o.user_id,
            products=o.products
        )
        for o in orders
    ]

@app.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return OrderResponse(
        order_id=order.id,
        user_id=order.user_id,
        products=order.products
    )

@app.put("/orders/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    order.user_id = order_update.user_id
    order.products = [p.dict() for p in order_update.products]
    db.commit()
    db.refresh(order)
    return OrderResponse(
        order_id=order.id,
        user_id=order.user_id,
        products=order.products
    )

@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    db.delete(order)
    db.commit()
    return {"message": "Pedido deletado com sucesso"}

