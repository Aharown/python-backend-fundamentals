from pydantic import BaseModel

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    read: bool

    class Config:
        from_attributes = True
