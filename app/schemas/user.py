from pydantic import BaseModel
from datetime import date
from typing import Optional


class UserCreateSchema(BaseModel):
    surname: str
    first_name: str
    photo: Optional[str] = None
    gender: str
    date_of_birth: date


class UserGetSchema(UserCreateSchema):
    user_id: int

    class Config:
        from_attributes = True


class UserUpdateSchema(BaseModel):
    surname: Optional[str] = None
    first_name: Optional[str] = None
    photo: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
