from sqlmodel import SQLModel, Field, Column
from datetime import datetime, date
import uuid
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy.sql import func


class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, default=uuid.uuid4)
    )

    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str

    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, server_default=func.now())
    )

    updated_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, server_default=func.now(), onupdate=func.now())
    )

    def __repr__(self):
        return f"<BOOK {self.title}>"
