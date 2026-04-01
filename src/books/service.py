from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel, BookUpdateModel
from sqlmodel import select, desc
from .schemas import Book


class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()

    async def get_particular_book(self, book_uid: str, session: AsyncSession):
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.exec(statement=statement)
        return result if result is not None else None

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        book_data_dict = book_data.model_dump()

    async def update_books(
        self, book_id: str, book_data: BookUpdateModel, session: AsyncSession
    ):
        # find the book to update
        book = await self.get_particular_book(book_uid=book_id, session=session)
        if book is not None:
            book_update_data = book_data.model_dump()

            for k, v in book_update_data.items():
                setattr(book, k, v)

            await session.commit
            await session.refresh(book)

            return book
        else:
            return None

    async def delete_books(self, book_uid: str, session: AsyncSession):
        book_to_delete = await self.get_particular_book(
            book_uid=book_uid, session=session
        )
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            return {}
        else:
            return None
