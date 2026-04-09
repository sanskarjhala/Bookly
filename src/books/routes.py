from typing import List
from fastapi import HTTPException, APIRouter, Depends, status
from src.books.schemas import BookUpdateModel, BookCreateModel,BookResponseModel
from src.books.service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.books.models import Book

book_router = APIRouter()
book_service = BookService()


@book_router.get("/all-books", response_model=List[BookResponseModel])
async def get_all_books(session: AsyncSession = Depends(get_session)) -> list:
    books = await book_service.get_all_books(session=session)
    return books


# Users Particular book
@book_router.get("/user/{user_id}", response_model=List[BookResponseModel])
async def get_user_books(user_id: str, session: AsyncSession = Depends(get_session)):
    pass


@book_router.get("/{book_uid}", response_model=BookResponseModel, status_code=status.HTTP_200_OK)
async def get_book_by_id(
    book_uid: str, session: AsyncSession = Depends(get_session)
) -> dict:
    result = await book_service.get_particular_book(book_uid=book_uid, session=session)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return result


@book_router.patch(
    "/update/{book_id}", response_model=BookResponseModel, status_code=status.HTTP_200_OK
)
async def update_book(
    book_uid: str,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
) -> dict:
    updated_book = await book_service.update_books(
        book_id=book_uid, book_data=book_update_data, session=session
    )
    if update_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found To update"
        )
    else:
        return updated_book


@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    book_to_delete = await book_service.delete_books(book_uid=book_uid, session=session)
    if book_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return {}


@book_router.post(
    "/create-book",
    # response_model=BookResponseModel,
    status_code=status.HTTP_201_CREATED
)
async def create_new_book(
    book_data: BookCreateModel,
    session: AsyncSession = Depends(get_session)
):
    result = await book_service.create_book(book_data, session)

    if result is None:
        raise HTTPException(status_code=500, detail="Book creation failed")

    return result
