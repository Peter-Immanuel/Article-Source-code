import datetime as dt
from uuid import UUID, uuid4
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
from enum import Enum



##Enumerators
class Gender(str, Enum):
   MALE = "MALE"
   FEMALE = "FEMALE"


class DevTools(BaseModel):
   language: str
   framework: Optional[List[str]]


class Employee(BaseModel):
   schema_version: int = 1
   document_version: int = 1
   id: UUID = Field(default_factory=uuid4)
   name:str
   gender: Gender
   email: EmailStr
   tools: Optional[List[str]] = None
   frameworks: Optional[List[str]] = None
   created_at: dt.datetime = dt.datetime.now()


class EmployeeDetails(BaseModel):
   name:str
   gender: Gender
   email: EmailStr
   tools: Optional[List[str]] = None
   frameworks: Optional[List[str]] = None
