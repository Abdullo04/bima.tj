from fastapi import APIRouter, Depends, HTTPException

from app.schemas.applications import ApplicationRequest
from app.schemas.core import APIResponse
from app.db.base import get_session
from app.services.application_service import ApplicationService

from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.post("", response_model=APIResponse)
async def application(request: ApplicationRequest, session: AsyncSession = Depends(get_session)):
    '''
    Create application
    :param request: ApplicationRequest obj
    :param session: Async session for DB
    :return: APIResponse obj
    '''
    service = ApplicationService(session)
    application_created = await service.create_application(
        request.full_name, request.phone_number, request.email, request.tariff, request.quote_id)

    if application_created is None:
        raise HTTPException(
            status_code=400, detail="Quote does not exists!")

    if not application_created:
        raise HTTPException(
            status_code=400, detail="Application already exists!")

    return APIResponse(success=True)


@router.get("/{id}")
async def application(id: int):
    return
