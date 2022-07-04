# FastAPI object is instantiated here
# Custom FastAPI configurations are done here.
import sys
from pathlib import Path
from fastapi import FastAPI
from .database.init_db import init_db
from .core.config import settings
from .api.deps import get_session
from .models.users import User

path = Path(__file__).parent.absolute()

sys.path.insert(0, str(path))


app = FastAPI()

@app.on_event("startup")
def on_startup():
   init_db()
   print("Database initialized")


# app.include_router(api_routers, prefix=settings.API_V1_STRING)
