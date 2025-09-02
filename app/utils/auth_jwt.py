from jwt import decode, encode
from datetime import datetime, timedelta

from app.config import config


def create_token(login: str, day: int = 1) -> str:
    '''
    Create JWT token
    :param login: User login
    :return: JWT token
    '''
    payload = {
        "sub": login,
        "exp": int((datetime.utcnow() + timedelta(days=day)).timestamp())
    }

    return encode(payload, config.jwt_secret_key, algorithm=config.jwt_algorithm)
