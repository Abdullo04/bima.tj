from fastapi import APIRouter, HTTPException, Depends

from app.schemas.core import RegisterRequest, APIResponse
from app.db.base import get_session
from app.models.core import User
from app.utils.hasher import verify_password, hash_password
from app.config import config

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


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

    query = select(User).where(User.login == request.login)
    user = await session.execute(query)
    if user.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(request.password, config.password_salt)

    new_user = User(
        first_name=request.first_name,
        last_name=request.last_name,
        login=request.login,
        password=hashed_password
    )

    session.add(new_user)
    await session.commit()
    return APIResponse(success=True)


@router.post("/auth/login")
async def login():
    '''
    Login user with JWT
    '''
    return
