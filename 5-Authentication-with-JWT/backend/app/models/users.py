import datetime as dt
from typing import Union
from sqlmodel import (
    Field, select,
    SQLModel
)
from uuid import UUID, uuid4
from pydantic import EmailStr
from .constants import GENDER




class UserCreate(SQLModel):
    username: str
    email: EmailStr
    password: str
    date_of_birth: dt.date


class User(UserCreate, table=True):
    id: UUID = Field(default=uuid4, primary_key=True)
    followers: int = Field(ge=0)
    following: int = Field(ge=0)
    created_at: dt.datetime = Field(default=dt.datetime.now)


class UserRead(SQLModel):
    id: UUID 
    username: str
    email: EmailStr
    date_of_birth: Union[dt.date, None]
    followers: int 
    following: int 
    created_at: dt.datetime


