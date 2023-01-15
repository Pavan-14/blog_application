from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# creating a database engine using sqlalchemy module
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# creating a session 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declare mapping (it will used in modely.py)
Base = declarative_base()


# connect to database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()