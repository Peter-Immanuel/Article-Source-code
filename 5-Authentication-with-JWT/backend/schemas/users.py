import datetime as dt
from sqlmodel import (
    Session, Field, select,
    SQLModel, create_engine
)
from uuid import UUID, uuid4
from pydantic import EmailStr


class User(SQLModel, table=True):
    id: UUID = Field(default=uuid4, primary_key=True)
    email: EmailStr
    username: str
    date_of_birth: dt.date
    gender: GENDER



