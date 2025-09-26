from datetime import datetime, timedelta
from typing import Annotated
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from config import settings
from schemas.auth_schemas import UserResponseSchema
from database import get_db
from tables.users import UsersTable

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = HTTPBearer()
db_dependency = Annotated[Session, Depends(get_db)]

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {
        "sub": username,
        "id": user_id,
        "exp": datetime.utcnow() + expires_delta
    }
    return jwt.encode(encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

def authenticate_user(db: Session, username: str, password: str):
    db_user = db.query(UsersTable).filter(UsersTable.username == username).first()
    if not db_user or not bcrypt_context.verify(password, db_user.password):
        return False
    return db_user

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError as e:
        print(f"Error decoding token: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request, session: Session = Depends(get_db)):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            payload = decode_jwt(token=credentials.credentials)
            if not payload:
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            user = session.query(UsersTable).filter(UsersTable.id == payload.get("id")).first()
            if user is None:
                raise HTTPException(status_code=403, detail="Invalid authorization code.")
            return UserResponseSchema.from_orm(user)  # Return Pydantic model
        raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        return decode_jwt(token=jwtoken) is not None