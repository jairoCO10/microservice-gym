
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from interfaces.gateways.UsersGateways import UserGateway
from core.use_cases.UserUseCase import UserUseCase
from entrypoints.schemas.UsersSchema import  UserCreate, UserReader
from infrastructure.database import Connect
from interfaces.dependencies import get_current_user


router = APIRouter()

@router.post("/register/", response_model=UserReader)
async def create_user(user: UserCreate, db: Session = Depends(Connect.get_db)):
    user_gateway = UserGateway(db)
    user_usecase = UserUseCase(user_gateway)
    return await user_usecase.create_user( user.email, user.username,  user.password,user.firstname,user.lastname,user.birthday,user.cellphone)


@router.get("/user/{user_id}")
async def get_user(user_id: int, db: Session = Depends(Connect.get_db)):
    # Aquí se haría la lógica para obtener el usuario de la base de datos
    user_gateway = UserGateway(db)
    user_usecase = UserUseCase(user_gateway)

    return await user_usecase.get_user(user_id)


@router.get("/users/")
async def get_users(db: Session = Depends(Connect.get_db), ):
    user_gateway = UserGateway(db)
    user_usecase = UserUseCase(user_gateway)
    return await user_usecase.get_users()