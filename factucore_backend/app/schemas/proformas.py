from datetime import date

from .common import ORMModel


class ProformaBase(ORMModel):
    pro_subtotal14: float = 0
    pro_subtotal0: float = 0
    pro_descuento: float = 0
    pro_subtotalSinImp: float = 0
    pro_iva0: float = 0
    pro_iva: float = 0
    pro_total: float
    pro_fecha: date
    pro_descripsion: str = ""
    pro_plazo: int = 0
    cliente_idCliente: int
    usuario_idUsuario: int
    comprobante: int
    pro_Estado: int = 1
    pro_tipoCredito: int = 0
    pro_Impuesto: int = 0
    pro_opiva: int = 0


class ProformaCreate(ProformaBase):
    pass


class ProformaUpdate(ORMModel):
    pro_subtotal14: float | None = None
    pro_subtotal0: float | None = None
    pro_descuento: float | None = None
    pro_subtotalSinImp: float | None = None
    pro_iva0: float | None = None
    pro_iva: float | None = None
    pro_total: float | None = None
    pro_fecha: date | None = None
    pro_plazo: int | None = None
    cliente_idCliente: int | None = None
    usuario_idUsuario: int | None = None
    comprobante: int | None = None
    pro_Estado: int | None = None
    pro_tipoCredito: int | None = None
    pro_Impuesto: int | None = None
    pro_opiva: int | None = None
    pro_descripsion: str | None = None


class ProformaRead(ProformaBase):
    idProforma: int
