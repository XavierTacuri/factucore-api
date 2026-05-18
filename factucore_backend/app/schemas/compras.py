from datetime import date

from .common import ORMModel


class ProveedorBase(ORMModel):
    proRuc: str
    proNombre: str
    proCiudad: str = ""
    proDireccion: str = ""
    proTelefono: str = ""
    proCelular: str = ""
    proMail: str = ""
    proBanco1: str = ""
    proBanco2: str = ""
    proCuenta1: str = ""
    proCuenta2: str = ""
    proTipoCuenta1: int = 0
    proTipoCuenta2: int = 0
    proProducto: str = ""
    proEstado: bool = True
    proColor: str = ""


class ProveedorCreate(ProveedorBase):
    pass


class ProveedorUpdate(ORMModel):
    proRuc: str | None = None
    proNombre: str | None = None
    proCiudad: str | None = None
    proDireccion: str | None = None
    proTelefono: str | None = None
    proCelular: str | None = None
    proMail: str | None = None
    proEstado: bool | None = None


class ProveedorRead(ProveedorBase):
    idProveedor: int


class FacturaProveedorBase(ORMModel):
    fpFactura: str
    fpSubtotal: float = 0
    fpSubtotal0: float = 0
    fpIva: float = 0
    fpTotal: float
    fpCredito: str = ""
    fpFecha: date
    fpPlazo: str = ""
    Usuario_idUsuario: int
    proveedor_idProveedor: int
    fpSaldo: float = 0
    fpAbono: float = 0


class FacturaProveedorCreate(FacturaProveedorBase):
    pass


class FacturaProveedorUpdate(ORMModel):
    fpFactura: str | None = None
    fpSubtotal: float | None = None
    fpSubtotal0: float | None = None
    fpIva: float | None = None
    fpTotal: float | None = None
    fpCredito: str | None = None
    fpFecha: date | None = None
    fpPlazo: str | None = None
    Usuario_idUsuario: int | None = None
    proveedor_idProveedor: int | None = None
    fpSaldo: float | None = None
    fpAbono: float | None = None


class FacturaProveedorRead(FacturaProveedorBase):
    idFacturaProveedor: int
