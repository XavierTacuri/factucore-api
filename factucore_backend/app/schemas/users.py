from pydantic import ConfigDict, Field

from .common import ORMModel


class UserCreate(ORMModel):
    userCedula: str
    userNombre: str
    userApellido: str
    userFono: str = ""
    userDireccion: str = ""
    userMail: str
    userUsuario: str
    password: str = Field(min_length=8)
    idRol: int


class UserUpdate(ORMModel):
    model_config = ConfigDict(from_attributes=True, extra="forbid")

    userNombre: str | None = None
    userApellido: str | None = None
    userFono: str | None = None
    userDireccion: str | None = None
    userEstado: bool | None = None


class UserRead(ORMModel):
    idUsuario: int
    userCedula: str
    userNombre: str
    userApellido: str
    userFono: str
    userDireccion: str
    userMail: str
    userUsuario: str
    userEstado: bool | None
    idRol: int
    rolNombre: str | None = None
