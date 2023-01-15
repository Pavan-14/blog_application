from typing import Union
from pydantic import EmailStr
from datetime import datetime, timedelta
from jose import jwt, JWTError
from blog import schemas


# using "openssl rand -hex 32" command gives SECRET_KEY
# HS256 is a symmetric algorithm that shares one secret key between the identity provider and your application.
# The same key is used to sign a JWT and allow verification that signature.

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# a utility function to generate a new access token.
def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()     #copied normal data to_encode variable
    
    if expires_delta: # if any expiration time provied
        expire = datetime.utcnow() + expires_delta

    else: # no expiration than add 30 minutes
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire}) # updating the dictionary with new expiration time
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # encoding the data using secret key, algorithm
    return encoded_jwt

# verify token
def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: EmailStr = payload.get("sub") # sub is key in dictonary used in authentication.py
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
