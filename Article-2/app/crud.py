#crud.py

from .database import get_database
from .schemas import Employee


database = get_database() #Create your connection
developer = database["developer"] #Create Collection


def add(employee: Employee):
   '''
   A function to create an Employee Document
   '''

   developer.insert_one(employee.dict())
   return employee 


def list(**filter):
   '''
   A function to get the list of Document based on a filter
   '''
   
   employee_list = developer.find(filter)
   return [Employee(**employee) for employee in employee_list]
