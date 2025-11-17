"""
Endpoints de usuario
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src. service.user_service import UserService
from src.repository.user_repository import UserRepository
from src.config.database import get_db
from src.models.user_model import CreateUsuario, UserResponse

user_router = APIRouter()


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
