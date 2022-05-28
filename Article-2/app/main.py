from typing import Union, List
from fastapi import (
   FastAPI, Query, 
   HTTPException, status, Depends
)
from .database import get_database
from .schemas import Employee, EmployeeDetails
from . import crud


app = FastAPI()



# present version 0.78.0
@app.post("/developer", response_model=Employee)
async def create_employee(developer: EmployeeDetails):
   try:
      new_employee = crud.add(Employee(**developer.dict()))
      return new_employee
   except Exception as e:
      raise HTTPException(
         status_code=status.HTTP_400_BAD_REQUEST,
         detail=f"Exception occured: {e}"
      )


@app.get("/developer", response_model=List[EmployeeDetails])
async def get_employees(
   languages: List[str] = Query(default=None),
   frameworks: List[str] = Query(default=None),
):
   try:
      
      language_query_list = {
            "tools": {"$in":languages}
         } if languages else {"tools":""}

      framework_query_list = {
            "frameworks":{"$in": frameworks}
         }  if frameworks else {"frameworks":""}    
      
      db_query =  {
            "$or":[
               language_query_list, 
               framework_query_list
            ]
         } 
      person_list = crud.list(**db_query)
      return person_list
   
   except Exception as e:
      raise HTTPException(
         status_code=status.HTTP_400_BAD_REQUEST,
         detail=f"Exception occured: {e}"
      )