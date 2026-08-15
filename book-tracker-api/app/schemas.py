from pydantic import BaseModel

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    read: bool

class BookCreate(BaseModel):
    title: str
    author: str
    read: bool = False

    class Config:
        from_attributes = True
