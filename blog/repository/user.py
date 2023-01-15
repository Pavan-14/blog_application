from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import models,schemas
from blog.hashing import Hash


def create_user(request: schemas.User, db: Session ):
    new_user = models.User(username=request.username, password=Hash.get_password_hash(request.password), email=request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} not available')
    return user