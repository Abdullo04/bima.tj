from fastapi import APIRouter, Depends, HTTPException

from app.schemas.quotes import QuoteRequest
from app.services.quote_service import CoefficientCalc, QuoteService
from app.schemas.core import APIResponse
from app.db.base import get_session

from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.post("", response_model=APIResponse)
async def quotes(request: QuoteRequest, session: AsyncSession = Depends(get_session)) -> APIResponse:
    '''
    Calculate qoute
    :param request: QuoteRequest obj
    :param session: Async session for DB
    :return: APIResponse obj
    '''
    service = CoefficientCalc(
        request.tariff, request.age, request.experience, request.car_type)
    price = service.calculate_coefficient()
    price = round(price, 2)
    quote_created = await QuoteService(session).create_quote(
        request.tariff, request.age, request.experience, request.car_type, price)

    if not quote_created:
        raise HTTPException(status_code=400, detail="Quote already exists")

    return APIResponse(success=True, data={"price": price})


@router.get("/{quote_id}", response_model=APIResponse)
async def quote(quote_id: int, session: AsyncSession = Depends(get_session)) -> APIResponse:
    '''
    Get quote by quote id
    :param quote_id: int
    :param session: Async session for DB
    :return: APIResponse obj
    '''
    quote = await QuoteService(session).get_quote(quote_id)

    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")

    return APIResponse(success=True, data={'id': quote_id, 'tariff': quote.tariff, 'age': quote.age, 'experience': quote.experience, 'car_type': quote.car_type, 'price': quote.price})
