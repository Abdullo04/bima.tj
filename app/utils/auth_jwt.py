from jwt import decode, encode
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
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


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    '''
    Decode JWT token and get username
    :param token: JWT token
    :return: Username
    '''
    try:
        decoded_token = decode(token, config.jwt_secret_key, algorithms=[
                               config.jwt_algorithm])
        return decoded_token["sub"]
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
