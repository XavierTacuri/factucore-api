from datetime import date

from .common import ORMModel


class OrdenTrabajoBase(ORMModel):
    doNumero: int
    doFechaIngreso: date
    doFechaSalida: date
    doTotal: float = 0
    doSaldo: float = 0
    doAbono: float = 0
    cliente_idCliente: int
    usuario_idUsuario: int
    doEstado: int = 1


class OrdenTrabajoCreate(OrdenTrabajoBase):
    pass


class OrdenTrabajoUpdate(ORMModel):
    doNumero: int | None = None
    doFechaIngreso: date | None = None
    doFechaSalida: date | None = None
    doTotal: float | None = None
    doSaldo: float | None = None
    doAbono: float | None = None
    cliente_idCliente: int | None = None
    usuario_idUsuario: int | None = None
    doEstado: int | None = None


class OrdenTrabajoRead(OrdenTrabajoBase):
    idOrden: int
