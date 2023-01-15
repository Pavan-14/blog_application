from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from blog import database,schemas,models, oauth 
from blog.repository import blog
from typing import List



# create router instance
router = APIRouter(prefix="/blog",tags=["Blog"])

# database connection function calling
get_db = database.get_db


@router.get('/', status_code=status.HTTP_200_OK,response_model=List[schemas.ShowBlog])
def show_all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.show_all_blogs(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BaseBlog,db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.create_blog(request,db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.delete(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.BaseBlog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.update_blog(id,request,db)


@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)): 
    return blog.show(id,db)

@router.get('/{id}/comments',status_code=status.HTTP_200_OK)
def comments(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return  blog.comments(id,db)
