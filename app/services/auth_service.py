from sqlalchemy import select

from app.models.core import User
from app.utils.hasher import verify_password
from app.config import config
from app.services.user_service import UserService


class AuthService:
    def __init__(self, session):
        self.session = session
        self.user_service = UserService(session)

    async def login(self, username: str, password: str):
        '''
        Login user
        :param username: Username
        :param password: Password
        :return: True if user logged in else False
        '''
        user = await self.user_service.user_exists(username)
        if not user:
            return False

        if not verify_password(password, user.password, config.password_salt):
            return False

        return True
