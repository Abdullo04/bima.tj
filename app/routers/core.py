from fastapi import APIRouter, HTTPException, Depends

from app.schemas.core import RegisterRequest, APIResponse, LoginRequest
from app.db.base import get_session
from app.utils.auth_jwt import create_token
from app.services.user_service import UserService
from app.services.auth_service import AuthService

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/auth/register", response_model=APIResponse)
async def register_user(request: RegisterRequest, session: AsyncSession = Depends(get_session)) -> APIResponse:
    '''
    Register new user
    :param request: RegisterRequest obj
    :param session: Session for DB
    :return: APIResponse obj
    '''
    if not request.password == request.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    user_created = await UserService(session).create_user(request)

    if not user_created:
        raise HTTPException(status_code=400, detail="User already exists")

    return APIResponse(success=True)


@router.post("/auth/login", response_model=APIResponse)
async def login(request: LoginRequest, session: AsyncSession = Depends(get_session)) -> APIResponse:
    '''
    Login user and get JWT token
    :param request: LoginRequest obj
    :param session: Async session for DB
    :return: APIResponse obj
    '''
    logged_in = await AuthService(session).login(request.username, request.password)

    if not logged_in:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_token(request.username)

    return APIResponse(success=True, data={"token": token})
