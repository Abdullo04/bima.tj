from pydantic import BaseModel, conint
from app.schemas.enums import Tariffs, CarTypes


class QuoteRequest(BaseModel):
    tariff: Tariffs
    age: conint(ge=18, le=100)
    experience: conint(ge=0, le=100)
    car_type: CarTypes
