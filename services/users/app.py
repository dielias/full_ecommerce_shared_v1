from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from services.shared.database import SessionLocal, engine
from services.shared.models import Base, User  # shared models/diretório
from services.users.schemas import UserCreate, UserUpdate, UserResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserResponse(
        user_id=db_user.user_id,
        name=db_user.name,
        email=db_user.email
    )

@app.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    stmt = select(User)
    users = db.execute(stmt).scalars().all()
    return [
        UserResponse(
            user_id=u.user_id,
            name=u.name,
            email=u.email
        )
        for u in users
    ]

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return UserResponse(
        user_id=user.user_id,
        name=user.name,
        email=user.email
    )

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    user.name = user_update.name
    user.email = user_update.email
    db.commit()
    db.refresh(user)
    return UserResponse(
        user_id=user.user_id,
        name=user.name,
        email=user.email
    )

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(user)
    db.commit()
    return {"message": "Usuário deletado com sucesso"}

