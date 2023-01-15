from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog import database,schemas
from blog.repository import user

# router instance
router = APIRouter(prefix="/user",tags=["User"])

# database connection 
get_db = database.get_db


# user part
@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request,db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    return user.show_user(id,db)
    