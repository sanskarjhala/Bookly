from typing import List
from fastapi import HTTPException, Header, APIRouter , status
from src.books.schemas import Book, BookUpdateModel
from src.books.book_Data import books_db


book_router = APIRouter()


@book_router.get("/headers")
async def headers(accept: str = Header(None), content_type: str = Header(None)):
    request_headers = {}
    request_headers["ACCEPT HEADERS"] = accept
    request_headers["Content-type"] = content_type

    return request_headers


@book_router.get("/", response_model=List[Book])
async def get_all_books() -> list:
    return books_db


@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books_db.append(new_book)
    return new_book


@book_router.get("/{book_id}")
async def update_the_book(book_id: int) -> dict:
    for book in books_db:
        if book["id"] == book_id:
            return book

    return HTTPException(status_code=404, detail="Book Not Found")


@book_router.patch("/{book_id}")
async def update_the_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    pass
