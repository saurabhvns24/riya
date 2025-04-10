from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    mobile: str
    address: Optional[str]

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

class ImageQueryCreate(BaseModel):
    user_id: int
    message: Optional[str]

class OrderCreate(BaseModel):
    user_id: int
    description: str

class PaymentCreate(BaseModel):
    user_id: int
    order_id: int
    amount: int