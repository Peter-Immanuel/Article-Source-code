from pydantic import BaseModel


class Book(BaseModel):
   name: str
   aurthor: str
   size: int
   download_count: int