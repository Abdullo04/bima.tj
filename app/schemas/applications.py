from pydantic import BaseModel, constr, EmailStr
from app.schemas.enums import Tariffs


class ApplicationRequest(BaseModel):
    full_name: constr(min_length=5)
    phone_number: constr(min_length=9, max_length=9, pattern=r'^\d{9}$')
    email: EmailStr
    tariff: Tariffs
    quote_id: int
