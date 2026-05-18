from pydantic import ConfigDict, EmailStr, Field

from .common import ORMModel


class ClientCreate(ORMModel):
    model_config = ConfigDict(from_attributes=True, extra="forbid")

    cedula: str = Field(min_length=1, max_length=13)
    cli_nombre: str = Field(min_length=1, max_length=80)
    cli_apellido: str = Field(min_length=1, max_length=80)
    cli_telefono: str = Field(default="", max_length=25)
    cli_direccion: str = Field(default="", max_length=55)
    cli_mail: EmailStr | None = None
    cli_descripcion: str = Field(default="", max_length=45)


class ClientRead(ORMModel):
    idCliente: int
    cedula: str
    cli_nombre: str
    cli_apellido: str
    cli_telefono: str
    cli_direccion: str
    cli_mail: str
    cli_descripcion: str


class ClientUpdate(ORMModel):
    model_config = ConfigDict(from_attributes=True, extra="forbid")

    cli_telefono: str | None = Field(default=None, max_length=25)
    cli_direccion: str | None = Field(default=None, max_length=55)
    cli_mail: EmailStr | None = None
    cli_descripcion: str | None = Field(default=None, max_length=45)
