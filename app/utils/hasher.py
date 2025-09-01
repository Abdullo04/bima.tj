from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str, salt: str = "") -> str:
    '''
    Convert password to hashed password
    :param password: Plain text password
    :param salt: Salt for hashing [Optional]
    :return: Hashed password
    '''
    return pwd_context.hash(password + salt)


def verify_password(password: str, hashed_password: str, salt: str = "") -> bool:
    '''
    Verify password
    :param password: Plain text password
    :param hashed_password: Hashed password
    :param salt: Salt for hashing [Optional]
    :return: True if password is correct
    '''
    return pwd_context.verify(password + salt, hashed_password)
