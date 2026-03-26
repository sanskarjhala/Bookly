from fastapi import FastAPI, Header, status, HTTPException
from src.books.routes import book_router


version = 'v1'

app = FastAPI(
    title="Bookly",
    description="A rest api for a book Review web service",
    version=version

)
app.include_router(book_router, prefix=f"/api/{version}/book")


@app.get("/")
def testing():
    return {"message": "Hi there"}
