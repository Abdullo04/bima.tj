from app.db.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey


class Applications(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    tariff = Column(String, nullable=False)
    quote = Column(Integer, ForeignKey("quotes.id"), nullable=False)
