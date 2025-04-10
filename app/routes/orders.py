
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, models, schemas

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    return {"msg": "order created"}

@router.get("/user/{user_id}")
def get_orders(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()