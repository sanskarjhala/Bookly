from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    published_year: int
    description: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    description: str