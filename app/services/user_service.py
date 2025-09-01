from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.core import User
from app.utils.hasher import hash_password, verify_password
from app.schemas.core import RegisterRequest
from app.config import config


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def user_exists(self, username: str):
        '''
        Check user exists
        :param username: Username
        :return: user if user exists else False
        '''
        query = select(User).where(User.username == username)
        user = await self.session.execute(query)
        user = user.scalar_one_or_none()
        return user if user else False

    async def create_user(self, user: RegisterRequest):
        '''
        Create new user
        :param user: RegisterRequest obj
        :return: True if user created else False
        '''
        if await self.user_exists(user.username):
            return False

        hashed_password = hash_password(user.password, config.password_salt)

        new_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            password=hashed_password
        )

        self.session.add(new_user)
        await self.session.commit()
        return True
