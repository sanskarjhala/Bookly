from pydantic import BaseModel
import uuid
from datetime import datetime , date
from typing import Optional


class BookSchema(BaseModel):
    uid: Optional[uuid.UUID] = None
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class BookCreateModel(BaseModel):
    title: str
    author:str
    publisher:str
    published_date: date
    page_count: int
    language : str

class BookUpdateModel(BaseModel):
    title: str
    author:str
    publisher:str
    page_count: int
    language : str



class BookResponseModel(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime