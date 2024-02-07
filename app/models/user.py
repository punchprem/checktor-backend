from pydantic import BaseModel
from typing import Optional
from app.database.connection import conn
from pydantic import EmailStr

class User(BaseModel):
    id: Optional[int] 
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    password: Optional[str] = None

