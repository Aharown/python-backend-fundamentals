from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Book
from app.schemas import BookResponse

app = FastAPI()

@app.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()
