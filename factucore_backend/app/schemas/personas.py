from .common import ORMModel


class ClienteBase(ORMModel):
    cedula: str
    cli_nombre: str
    fono: str = ""
    direccion: str = ""
    c_descripcion: str = ""
    cli_mail: str = ""


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(ORMModel):
    cedula: str | None = None
    cli_nombre: str | None = None
    fono: str | None = None
    direccion: str | None = None
    c_descripcion: str | None = None
    cli_mail: str | None = None


class ClienteRead(ClienteBase):
    idCliente: int


class UsuarioBase(ORMModel):
    userCedula: str
    userNombre: str
    userApellido: str
    userFono: str = ""
    userDireccion: str = ""
    userFecha: str = ""
    userMail: str
    userUsuario: str
    userEstado: bool | None = True
    userPrincipal: bool | None = False
    idRol: int


class UsuarioCreate(UsuarioBase):
    userClave: str


class UsuarioUpdate(ORMModel):
    userCedula: str | None = None
    userNombre: str | None = None
    userApellido: str | None = None
    userFono: str | None = None
    userDireccion: str | None = None
    userFecha: str | None = None
    userMail: str | None = None
    userUsuario: str | None = None
    userClave: str | None = None
    userEstado: bool | None = None
    userPrincipal: bool | None = None
    idRol: int | None = None


class UsuarioRead(UsuarioBase):
    idUsuario: int
