# schemas.py pydantic models

import datetime as dt
from uuid import UUID, uuid4
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
from enum import Enum



class Gender(str, Enum):
   '''
   Enum class for Gender
   '''
   
   MALE = "MALE"
   FEMALE = "FEMALE"



class Employee(BaseModel):
   '''
   Pydantic Model for Employee
   '''
   
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
   '''
   Pydantic model used to collect data from frontend
   '''
   
   name:str
   gender: Gender
   email: EmailStr
   tools: Optional[List[str]] = None
   frameworks: Optional[List[str]] = None
