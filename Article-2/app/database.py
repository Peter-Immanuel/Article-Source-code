from pymongo import MongoClient 

DATABASE_URL = 'mongodb://localhost:27017/'

# establish a connection
client = MongoClient(DATABASE_URL, uuidRepresentation="standard")

# create your db

database = client["employee"]

def get_database():
   return database





