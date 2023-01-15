# Union and optional are used for same purpose. better to use Union
from typing import Optional, List, Union
from pydantic import BaseModel, EmailStr

# login request schema
class Login(BaseModel):
    username: EmailStr
    password: str

# blog schemas (requset)
class BaseBlog(BaseModel):
    title: str
    body: str
    published: Optional[str] = None

# this class useful for realtionship purpose
class Blog(BaseModel):
    title: str
    class Config():
        orm_mode = True


# user schemas (request)
class User(BaseModel):
    username: str
    password: str
    email: EmailStr

# user response schema
class ShowUser(BaseModel):
    username: str
    email: EmailStr
    # relationship from models.py(you need to dispaly owner of the blogs )
    blogs: List["Blog"] = []

    class Config:
       orm_mode = True

# this class useful for creator realtionship purpose
class ShowUserRelation(BaseModel):
    username: str
    email: EmailStr
    class Config:
        orm_mode = True

# blog response schema
class ShowBlog(BaseModel):
    title: str
    # creator from models.py (relationship)
    creator: ShowUserRelation
    class Config:
        orm_mode = True


# token schema
class Token(BaseModel):
    access_token: str
    token_type: str

# this used in token verification in jtoken.py file
class TokenData(BaseModel):
    email: Union[EmailStr, None] = None