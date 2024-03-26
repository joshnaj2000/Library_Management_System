from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    fname: Optional[str] = None
    lname: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None
    borrowed_books:Optional[list]=None

class Book(BaseModel):
    isbn: Optional[str] = None
    Title: Optional[str] = None
    Author: Optional[str] = None
    Publisher: Optional[str] = None
    Availability: Optional[int] = None
