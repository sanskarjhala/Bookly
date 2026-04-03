from sqlmodel import SQLModel, Field, Column
from datetime import datetime, date
from typing import Optional
import uuid
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy.sql import func


class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(pg.UUID, primary_key=True, default=uuid.uuid4, nullable=False)
    )

    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str

    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(pg.TIMESTAMP, server_default=func.now(), nullable=False)
    )

    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            pg.TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False
        )
    )

    def __repr__(self):
        return f"<BOOK {self.title}>"