# Dependencies All Dependencies including
# database, user, active, cache etc.
from app.database.init_db import engine
from sqlmodel import Session
 

def get_session():
   with Session(engine) as session:
      yield session