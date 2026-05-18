from pydantic import BaseModel

from .common import ORMModel


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenPayload(BaseModel):
    sub: str
    username: str | None = None
    role: str | None = None
    exp: int | None = None


class CurrentUserResponse(ORMModel):
    idUsuario: int
    userUsuario: str
    userNombre: str
    userApellido: str
    userMail: str
    userEstado: bool | None
    idRol: int
    rolNombre: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: CurrentUserResponse
