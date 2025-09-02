from app.models.applications import Applications
from app.services.quote_service import QuoteService
from sqlalchemy import select


class ApplicationService:
    def __init__(self, session):
        self.session = session
        self.quote_service = QuoteService(session)

    async def create_application(self, full_name: str, phone_number: str, email: str, tariff: str, quote_id: int):
        quote_exists = await self.quote_service.get_quote(quote_id)
        if not quote_exists:
            return None

        query = select(Applications).where(
            Applications.full_name == full_name,
            Applications.phone_number == phone_number,
            Applications.email == email,
            Applications.tariff == tariff,
            Applications.quote == quote_id
        )
        application = await self.session.execute(query)
        application = application.scalar_one_or_none()
        if application:
            return False

        self.session.add(Applications(
            full_name=full_name,
            phone_number=phone_number,
            email=email,
            tariff=tariff,
            quote=quote_id
        ))
        await self.session.commit()
        return True
