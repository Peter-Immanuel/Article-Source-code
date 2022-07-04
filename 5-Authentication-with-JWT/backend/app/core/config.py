import os, secrets
from pydantic import BaseSettings
from dotenv import load_dotenv




load_dotenv()


class Settings(BaseSettings):
   ALGORITHM: str = "HS256"
   DATABASE_URL: str = os.environ.get("DATABASE_URL")
   SECRET_KEY: str = secrets.token_urlsafe(32)

   API_V1_STRING: str = "/api/v1"


   # Super user details
   FIRST_SUPERUSER_USERNAME: str = os.environ.get("FIRST_SUPERUSER_NAME")
   FIRST_SUPERUSER_EMAIL: str = os.environ.get("FIRST_SUPERUSER_EMAIL")
   FIRST_SUPERUSER_PASSWORD: str = os.environ.get("FIRST_SUPERUSER_PASSWORD")


   




settings = Settings()

