from datetime import datetime, timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from utils.auth_utils import JWTBearer, bcrypt_context, authenticate_user, create_access_token
from schemas import auth_schemas as schemas_users
from tables.users import UsersTable
from database import get_db
from config import settings

router = APIRouter(prefix="/auth", tags=['Auth'])
db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(db: db_dependency, create_user_schema: schemas_users.CreateUserSchema):
    try:
        create_user_model = UsersTable(
            username=create_user_schema.username,
            password=bcrypt_context.hash(create_user_schema.password),
            first_name=create_user_schema.first_name,
            last_name=create_user_schema.last_name,
            phone_number=create_user_schema.phone_number,
        )
        db.add(create_user_model)
        db.commit()
        db.refresh(create_user_model)
        return {"message": f"Successfully registered {create_user_schema.first_name} {create_user_schema.last_name}"}
    except IntegrityError as e:
        detail = str(e.orig)  # Get the raw PostgreSQL error message
        if "users_username_key" in detail:
            detail = "Username already exists"
        elif "users_phone_number_key" in detail:
            detail = "Phone number already exists"
        else:
            detail = f"Database constraint error: {detail}"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

@router.post('/token/', response_model=schemas_users.TokenSchema, status_code=status.HTTP_200_OK)
async def signin_by_access_token(db: db_dependency, data: schemas_users.UserLoginSchema):
    user = authenticate_user(db, data.username, data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    token = create_access_token(user.username, user.id, timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    return {
        'access_token': token,
        'token_type': 'Bearer'
    }

@router.get("/me/", response_model=schemas_users.UserResponseSchema, status_code=status.HTTP_200_OK)
async def get_me(current_user: schemas_users.UserResponseSchema = Depends(JWTBearer())):
    return current_user

@router.put("/password/change", status_code=status.HTTP_201_CREATED, response_model=schemas_users.UserResponseSchema)
async def change_password(db: db_dependency, user_ver: schemas_users.UserVerifications, current_user: schemas_users.UserResponseSchema = Depends(JWTBearer())):
    user = db.query(UsersTable).filter(UsersTable.id == current_user.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not bcrypt_context.verify(user_ver.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong password")
    
    user.password = bcrypt_context.hash(user_ver.new_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user