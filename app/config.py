from dotenv import load_dotenv

import os

load_dotenv(override=True)


class Config:
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_host: str = os.getenv("DB_HOST")
    db_port: str = os.getenv("DB_PORT")
    db_name: str = os.getenv("DB_NAME")
    password_salt: str = os.getenv("PASSWORD_SALT")
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM")
    jwt_day_expire: int = int(os.getenv("JWT_DAY_EXPIRE"))


config = Config()
