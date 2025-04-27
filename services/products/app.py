from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from shared.database import SessionLocal, engine
from shared.models import Base, Product

app = FastAPI()

# Garante que as tabelas sejam criadas no banco
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products")
def create_product(name: str, price: int, db: Session = Depends(get_db)):
    product = Product(name=name, price=price)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@app.get("/products")
def list_products(db: Session = Depends(get_db)):
    stmt = select(Product)
    products = db.execute(stmt).scalars().all()
    return products

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    db.delete(product)
    db.commit()
    return {"message": "Produto deletado com sucesso"}

# 🔥 Nova rota para atualizar produto
@app.put("/products/{product_id}")
def update_product(product_id: int, name: str, price: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    product.name = name
    product.price = price
    db.commit()
    db.refresh(product)
    return product
