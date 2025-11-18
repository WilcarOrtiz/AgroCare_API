"""
Servicio Usuario
"""
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from passlib.context import CryptContext
from jose import jwt
import bcrypt
from src.repository.user_repository import UserRepository
from src.models.user_model import CreateUsuario


load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuración JWT
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30))


class UserService:
    """
    Logica referente a la gestion de usuarios
    """

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_password_hasd(self, password: str) -> str:
        """
        Generacion de la contraseña hasehada
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verificar que la contraseña conincide con el hash
        """
        return bcrypt.checkpw(plain_password.encode('utf-8'),
                              hashed_password.encode('utf-8'))

    def create_user(self, usuario: CreateUsuario):
        """
        Servicio de creacion de usuario 
        """
        usuario.password = self.get_password_hasd(usuario.password)
        return self.repo.crear(usuario)

    def login(self, username: str, password: str):
        """
        Servicio de acceso al sistema
        """
        user = self.repo.login(username)
        if not user:
            raise ValueError("Credenciales incorrectas")

        is_valid = self.verify_password(password, user.password)

        if not is_valid:
            raise ValueError("Credenciales incorrectas")

        access_token = self._create_access_token(
            data={
                "sub": user.username,
                "user_id": user.id,
                "user_email": user.email,
                "user_role": user.role
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    def _create_access_token(self, data: dict) -> str:
        """
        Crea un token JWT
        """
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + \
            timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
