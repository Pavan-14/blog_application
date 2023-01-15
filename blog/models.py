from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship 
from blog.database import Base

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    published = Column(String)
    # relationship
    user_id = Column(Integer,ForeignKey("users.id"))
    creator = relationship("User",back_populates="blogs") # using many to one bidirectional behavior


# user table

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    # relationship
    blogs = relationship("Blog",back_populates="creator")
