from fastapi import APIRouter, HTTPException, Depends
from ..schemas.core import RegisterRequest, APIResponse
from ..db.base import get_session
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.post("/auth/register")
async def register_user(request: RegisterRequest, session: AsyncSession = Depends(get_session)) -> APIResponse:
    '''
    Register new user
    :param request: RegisterRequest obj
    :param session: Session for DB
    :return: APIResponse obj
    '''
    if not request.password == request.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")


@router.post("/auth/login")
async def login():
    '''
    Login user with JWT
    '''
    return
