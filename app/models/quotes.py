from sqlalchemy import Column, String, Integer, Float
from app.db.base import Base


class Quotes(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tariff = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    experience = Column(Integer, nullable=False)
    car_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
