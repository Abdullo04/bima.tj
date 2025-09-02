from fastapi import APIRouter, Depends, HTTPException

from app.schemas.applications import ApplicationRequest
from app.schemas.core import APIResponse
from app.db.base import get_session
from app.services.application_service import ApplicationService
from app.utils.auth_jwt import get_current_user

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


@router.get("/{application_id}", response_model=APIResponse)
async def application(application_id: int, session: AsyncSession = Depends(get_session), user: str = Depends(get_current_user)) -> APIResponse:
    '''
    Get application by id
    :param application_id: Id of application
    :param session: Async session for DB
    :param user: Returns current user username
    :return: APIResponse obj
    '''
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    service = ApplicationService(session)
    application = await service.get_application(application_id)

    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")

    return APIResponse(success=True, data={'fullname': application.full_name, 'phone_number': application.phone_number, 'email': application.email, 'tariff': application.tariff, 'quote_price': application.quote_price})
