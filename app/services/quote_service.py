from app.schemas.enums import Tariffs, CarTypes
from app.models.quotes import Quotes
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class QuoteService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_quote(self, tariff: str, age: int, experience: int, car_type: str, price: float):
        query = select(Quotes).where(
            Quotes.tariff == tariff,
            Quotes.age == age,
            Quotes.experience == experience,
            Quotes.car_type == car_type
        )
        quote = await self.session.execute(query)
        quote = quote.scalar_one_or_none()
        if quote:
            return False

        quote = Quotes(
            tariff=tariff,
            age=age,
            experience=experience,
            car_type=car_type,
            price=price
        )

        new_quote = Quotes(
            tariff=tariff,
            age=age,
            experience=experience,
            car_type=car_type,
            price=price
        )
        self.session.add(new_quote)
        await self.session.commit()
        return True

    async def get_quote(self, quote_id: int):
        query = select(Quotes).where(Quotes.id == quote_id)
        quote = await self.session.execute(query)
        quote = quote.scalar_one_or_none()
        return quote


class CoefficientCalc:
    TARIFF_COEFFICIENT = {
        Tariffs.BASIC: 500,
        Tariffs.STANDART: 1000,
        Tariffs.PREMIUM: 1500
    }

    AGE_COEFFICIENT = {
        '18_to_22': 1.5,
        '23_to_30': 1.3,
        '31_to_40': 1.1,
        '41_to_100': 1.0
    }

    EXPERIENCE_COEFFICIENT = {
        '0_to_5': 1.5,
        '6_to_10': 1.3,
        '11_to_15': 1.1,
        '16_to_100': 1.0
    }

    CAR_TYPE_COEFFICIENT = {
        CarTypes.CAR: 1.1,
        CarTypes.VAN: 1.3,
        CarTypes.TRUCK: 1.5
    }

    def __init__(self, tariff: Tariffs, age: int, experience: int, car_type: CarTypes):
        self.tariff = tariff
        self.age = age
        self.experience = experience
        self.car_type = car_type

    def calculate_coefficient(self):
        # стоимость = базовая_ставка_тарифа * коэффициент_возраста * коэффициент_стажа * коэффициент_типа
        if self.age in range(18, 23):
            age_exp = '18_to_22'
        elif self.age in range(23, 31):
            age_exp = '23_to_30'
        elif self.age in range(31, 41):
            age_exp = '31_to_40'
        elif self.age in range(41, 101):
            age_exp = '41_to_100'

        if self.experience in range(0, 6):
            experience = '0_to_5'
        elif self.experience in range(6, 11):
            experience = '6_to_10'
        elif self.experience in range(11, 16):
            experience = '11_to_15'
        elif self.experience in range(16, 101):
            experience = '16_to_100'

        return self.TARIFF_COEFFICIENT[self.tariff] * self.AGE_COEFFICIENT[age_exp] * self.EXPERIENCE_COEFFICIENT[experience] * self.CAR_TYPE_COEFFICIENT[self.car_type]
