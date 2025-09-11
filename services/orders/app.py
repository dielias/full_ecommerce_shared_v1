from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from services.shared.database import SessionLocal, engine
from services.shared.models import Base, Order
from services.orders.schemas import OrderCreate, OrderUpdate, OrderResponse
from services.shared.models import User, Product, Order


app = FastAPI()

# Cria as tabelas se não existirem
Base.metadata.create_all(bind=engine)

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@app.post("/orders", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    # Valida user_id
    user = db.get(User, order.user_id)
    if not user:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")
    
    # Valida product_id
    product = db.get(Product, order.product_id)
    if not product:
        raise HTTPException(status_code=400, detail="Produto não encontrado")
    
    db_order = Order(user_id=order.user_id, product_id=order.product_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@app.get("/orders", response_model=List[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return [
        OrderResponse(order_id=o.order_id, user_id=o.user_id, product_id=o.product_id)
        for o in orders
    ]

@app.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.get(Order, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return OrderResponse(
        order_id=db_order.id,
        user_id=db_order.user_id,
        product_id=db_order.product_id
    )

@app.put("/orders/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)):
    db_order = db.get(Order, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    db_order.user_id = order_update.user_id
    db_order.product_id = order_update.product_id
    db.commit()
    db.refresh(db_order)
    return OrderResponse(
        order_id=db_order.id,
        user_id=db_order.user_id,
        product_id=db_order.product_id
    )

@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.get(Order, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    db.delete(db_order)
    db.commit()
    return {"message": "Pedido deletado com sucesso"}

