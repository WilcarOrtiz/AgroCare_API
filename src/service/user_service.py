"""
Servicio Usuario
"""
from src.repository.user_repository import UserRepository
from src.models.user_model import CreateUsuario


class UserService:
    """
    Logica referente a la gestion de usuarios
    """

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, usuario: CreateUsuario):
        """
        Servicio de creacion de usuario 
        """
        return self.repo.crear(usuario)
