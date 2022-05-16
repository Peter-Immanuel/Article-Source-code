from fastapi import FastAPI, Query
from .schema import Book


app = FastAPI()

books_db = {
   "book1": 15,
   "book2": 20,
   "book3": 9
}


# previous version 
@app.get("/book-page-old/")
async def get_books_pages(books: list = Query(...)):
   '''
   This function provides the number of pages per book.
   Previous FastAPI release 0.77.1 below
   '''
   response = {}
   for book in books:
      response.update(
         {book:books_db[book]}
      )
   return response



# present version 0.78.0
@app.get("/book-page-new/")
async def get_book_pages(books: list = Query(exclusiveMaximum=3)):
   '''
   This function provides the number of pages per book.
   New FastAPI release 0.78.0 
   '''
   response = {}
   for book in books:
      response.update(
         {book:books_db[book]}
      )
   return response



@app.get("/book-size/")
async def get_books_size(size: int=Query()):
   return {
      "Book size": size,
   }
