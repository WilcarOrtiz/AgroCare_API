"""
Endpoints de usuario
"""
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.user_model import CreateUsuario, UserResponse
from src.repository.user_repository import UserRepository
from src.service.user_service import UserService

user_router = APIRouter()
oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def get_usuario_service(db: Session = Depends(get_db)):
    """
    Funcion para inyectar dependencias
    """
    repo = UserRepository(db)
    return UserService(repo)


@user_router.post('/', response_model=UserResponse, status_code=201)
def create_user(
        user: CreateUsuario,
        servicio: UserService = Depends(get_usuario_service)
):
    """
    Obtener los usuarios
    """
    try:
        user_created = servicio.create_user(user)
        return user_created
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@user_router.post('/token')
def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        servicio: UserService = Depends(get_usuario_service)):
    """
    Endpoind de inicio de sesion
    """
    try:
        user = servicio.login(form_data.username, form_data.password)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e
