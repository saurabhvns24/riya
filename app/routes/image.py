from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from app import database, models
import shutil, os

router = APIRouter(prefix="/image", tags=["Image"])
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
def upload(user_id: int = Form(...), message: str = Form(""), file: UploadFile = File(...), db: Session = Depends(get_db)):
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    query = models.ImageQuery(user_id=user_id, image_path=path, message=message)
    db.add(query)
    db.commit()
    return {"msg": "uploaded", "image": path}