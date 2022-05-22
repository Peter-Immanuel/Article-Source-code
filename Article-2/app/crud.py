from .database import get_database
from .schemas import Employee

#Create your connection
database = get_database()

developer = database["developer"]


# function to create a human object
def add(employee: Employee):
   print(employee)
   developer.insert_one(employee.dict())
   return employee 


#function to get a list of objects based on filter
def list(**filter):
   employee_list = developer.find(filter)
   return [Employee(**employee) for employee in employee_list]
