from app.core.config import settings
from sqlmodel import (
   SQLModel, create_engine, Session
)

engine = create_engine(settings.DATABASE_URL, echo=True)


def init_db():
   SQLModel.metadata.create_all(engine)

   # create the firstsuperuser

    
