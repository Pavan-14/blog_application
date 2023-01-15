from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog import schemas,database,models
from blog.hashing import Hash
from blog.jtoken import create_access_token

# router instance
router = APIRouter(prefix="/login",tags=['Authentication'])

# database connection instance
get_db = database.get_db
 

@router.post("/",status_code=status.HTTP_201_CREATED)
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    # checking user available or not
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid user')
    
    # conforming the password
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Incorrect Password')
    
    # call the function to get access token (JWT Token)
    access_token = create_access_token(data={"sub":user.email}) # user.email from query object
    return {"access_token": access_token, "token_type": "bearer"}
    