"""
USUARIO
"""
from sqlalchemy import Column, Enum, Integer, String
from src.models.user_model import RolesEnum
from src.config.database import Base


class UserSchema(Base):
    """
    Esquema de USUARIO en la base de datos
    """
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    identificacion = Column(String, unique=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(RolesEnum), nullable=False,
                  default=RolesEnum.AGRICULTOR)
