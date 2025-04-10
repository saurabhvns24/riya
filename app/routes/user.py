from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, models, database

router = APIRouter(prefix="/user", tags=["User"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(mobile=user.mobile, address=user.address)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/profile/{mobile}")
def profile(mobile: str, db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.mobile == mobile).first()