from jwt import decode, encode
from datetime import datetime, timedelta

from app.config import config


def create_token(login: str) -> str:
    payload = {
        "sub": login,
        "exp": int((datetime.utcnow() + timedelta(days=1)).timestamp())
    }

    return encode(payload, config.jwt_secret_key, algorithm=config.jwt_algorithm)
