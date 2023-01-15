from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from blog import schemas,models


def show_all_blogs(db: Session):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'no blogs available')
    return blogs

def create_blog(request: schemas.BaseBlog,db: Session):
    new_blog = models.Blog(title=request.title,body=request.body,published=request.published,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'the blog with id {id} not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'deatil':f'deleted blog id {id}'}

def update_blog(id: int, request: schemas.BaseBlog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not available')
    blog.update(request.dict())
    # the put operation updates the old record with new record
    # if you want to update only few attributes in record the go for patch
    db.commit()
    return 'blog updated'

def show(id, db: Session): 
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not available')
    return blog


def comments(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not available')
    return {'detail':f'blog {id} comments'}
