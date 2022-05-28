# database.py

from pymongo import MongoClient 

# This should be kept as environment variable
DATABASE_URL = 'mongodb://localhost:27017/'

# Create a client
client = MongoClient(DATABASE_URL, uuidRepresentation="standard")


# Create Database
database = client["employee"]

def get_database():
   return database





