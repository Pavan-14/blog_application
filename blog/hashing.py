from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    # to hassh the password
    def get_password_hash(password: str):
        return pwd_context.hash(password)
    
    # to compare the passwords
    def verify(hashed_password, request_plain_password):
        return pwd_context.verify(request_plain_password,hashed_password)