from pydantic import BaseModel
from typing import Optional


class LoginRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    confirm_password: str


class ErrorDetail(BaseModel):
    code: int
    message: str


class APIResponse(BaseModel):
    success: bool
    data: Optional[dict] = None
    error: Optional[ErrorDetail] = None
