# pylint: disable=no-self-argument
"""
Modelos USUARIO
"""
from enum import Enum
import re
from pydantic import BaseModel, Field, EmailStr, field_validator


class RolesEnum(str, Enum):
    """
    Enumeracion de roles del sistema
    """
    AGRICULTOR = "agricultor"
    ADMINISTRADOR = "administrador"


class Usuario(BaseModel):
    """
    Esquema completo del usuario (respuesta o almacenamiento)
    """
    identificacion: str
    username: str
    email: EmailStr
    password: str
    role: RolesEnum


class CreateUsuario(BaseModel):
    """
    Esquema de creación de usuario con validaciones
    """
    identificacion: str = Field(min_length=5, max_length=11)
    username: str = Field(min_length=5)
    email: EmailStr
    password: str
    role: RolesEnum

    @field_validator("username")
    def validar_username(cls, value):
        """
        Username sin espacios y mínimo 5 caracteres.
        """
        if " " in value:
            raise ValueError("El username no puede contener espacios.")
        return value

    @field_validator("password")
    def validar_password(cls, value):
        """
        Validación de contraseña segura:
        - Mínimo 8 caracteres
        - Al menos una mayúscula
        - Al menos una minúscula
        - Al menos un número
        - Al menos un carácter especial
        """
        if len(value) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")

        if not re.search(r"[A-Z]", value):
            raise ValueError(
                "La contraseña debe contener al menos una letra mayúscula.")

        if not re.search(r"[a-z]", value):
            raise ValueError(
                "La contraseña debe contener al menos una letra minúscula.")

        if not re.search(r"[0-9]", value):
            raise ValueError("La contraseña debe contener al menos un número.")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError(
                "La contraseña debe contener al menos un carácter especial.")

        return value


class UserResponse(BaseModel):
    """
    Esquema de respuesta
    """
    id: int
    identificacion: str
    username: str
    email: EmailStr
    role: RolesEnum

    class Config:
        """
        permite usar objetos SQLAlchemy directamente
        """
        orm_mode = True
