from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = "6e5fa3415403d7e245e17f2ae176fe62aae6907bde0a5f37c82530811287f7d9"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES =1600

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return payload
     
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)



async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload