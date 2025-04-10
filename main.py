from fastapi import FastAPI
from app.routes import user, image, orders, payments, metal 
from app.database import create_db_and_tables

app = FastAPI(title="Riya Jewellers API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(user.router)
app.include_router(image.router)
app.include_router(orders.router)
app.include_router(payments.router)
app.include_router(metal.router)

