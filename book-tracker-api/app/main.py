from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Book
from app.schemas import BookResponse
from app.schemas import BookCreate


app = FastAPI()

@app.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@app.post("/books", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
