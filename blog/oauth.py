from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from blog import jtoken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") # login path 

def get_current_user(token_data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return jtoken.verify_token(token_data,credentials_exception)
