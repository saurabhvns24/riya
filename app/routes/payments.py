from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, schemas, models

router = APIRouter(prefix="/payments", tags=["Payments"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/pay")
def make_payment(data: schemas.PaymentCreate, db: Session = Depends(get_db)):
    payment = models.Payment(**data.dict(), status="initiated")
    db.add(payment)
    db.commit()
    return {"msg": "payment initiated"}