"""
REPOSITORIO USUARIO
"""
from sqlalchemy.orm import Session

from src.schema.user_db import UserSchema
from src.models.user_model import CreateUsuario


class UserRepository:
    """
    METODOS DE REPOSITORIO
    """

    def __init__(self, db: Session):
        self.db = db

    def crear(self, usuario: CreateUsuario) -> UserSchema:
        """
        Creacion de usuario en base de datos
        """
        usuario_db = UserSchema(
            identificacion=usuario.identificacion,
            username=usuario.username,
            email=usuario.email,
            password=usuario.password,
            role=usuario.role
        )
        self.db.add(usuario_db)
        self.db.commit()
        self.db.refresh(usuario_db)
        return usuario_db
