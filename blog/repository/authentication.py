"""
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import schemas,models

def login(request:schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    # checking user available or not
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid user')
    return user
"""