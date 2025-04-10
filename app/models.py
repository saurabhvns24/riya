from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    mobile = Column(String(15), unique=True)
    address = Column(String(255))
    token = Column(String(255))

class ImageQuery(Base):
    __tablename__ = 'image_queries'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    image_path = Column(String(255))
    message = Column(Text)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(Text)
    image_path = Column(String(255))
    status = Column(String(50), default="pending")

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    order_id = Column(Integer)
    amount = Column(Integer)
    status = Column(String(50))