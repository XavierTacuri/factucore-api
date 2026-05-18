from datetime import date

from .common import ORMModel


class FacturaBase(ORMModel):
    subtotal14: float = 0
    subtotal0: float = 0
    descuento: float = 0
    subtotalSinImp: float = 0
    iva0: float = 0
    iva: float = 0
    total: float
    fecha: date
    descripsion: str = ""
    plazo: int = 0
    fEntrada: float = 0
    fSaldo: float = 0
    utilidad: float = 0
    cliente_idCliente: int
    credito_idCreditoCliente: int = 0
    usuario_idUsuario: int
    secuencia: int
    ptoEmicion: int
    establecimiento: int
    comprobante: int
    facEstado: int = 1
    tipoCredito: int = 0
    facImpuesto: int = 0
    fac_claveacceso: str = ""
    fac_sriestado: str = ""
    fac_enviocliente: int = 0


class FacturaCreate(FacturaBase):
    pass


class FacturaUpdate(ORMModel):
    subtotal14: float | None = None
    subtotal0: float | None = None
    descuento: float | None = None
    subtotalSinImp: float | None = None
    iva0: float | None = None
    iva: float | None = None
    total: float | None = None
    fecha: date | None = None
    descripsion: str | None = None
    plazo: int | None = None
    fEntrada: float | None = None
    fSaldo: float | None = None
    utilidad: float | None = None
    cliente_idCliente: int | None = None
    credito_idCreditoCliente: int | None = None
    usuario_idUsuario: int | None = None
    secuencia: int | None = None
    ptoEmicion: int | None = None
    establecimiento: int | None = None
    comprobante: int | None = None
    facEstado: int | None = None
    tipoCredito: int | None = None
    facImpuesto: int | None = None
    fac_claveacceso: str | None = None
    fac_sriestado: str | None = None
    fac_enviocliente: int | None = None


class FacturaRead(FacturaBase):
    idFactura: int


class DetalleBase(ORMModel):
    cantidad: int
    codPrincipal: str
    descripcion: str
    valorUnitario: float
    det_descuento: float = 0
    valorTotal: float
    factura_idFactura: int
    inventario_idInventario: int
    idVenta: int = 0
    idOrdenTrabajo: int = 0
    detValorConImpuesto: float = 0
    idTalla: int = 0
    idSerie: int = 0


class DetalleCreate(DetalleBase):
    pass


class DetalleUpdate(ORMModel):
    cantidad: int | None = None
    codPrincipal: str | None = None
    descripcion: str | None = None
    valorUnitario: float | None = None
    det_descuento: float | None = None
    valorTotal: float | None = None
    factura_idFactura: int | None = None
    inventario_idInventario: int | None = None
    idVenta: int | None = None
    idOrdenTrabajo: int | None = None
    detValorConImpuesto: float | None = None
    idTalla: int | None = None
    idSerie: int | None = None


class DetalleRead(DetalleBase):
    idDetalle: int


class CreditoBase(ORMModel):
    creditoFecha: date
    creditoEntrada: float
    creditoSaldo: float
    creditoTotal: float
    Cliente_idCliente: int
    Usuario_idUsuario: int
    creditoEstado: int = 1


class CreditoCreate(CreditoBase):
    pass


class CreditoUpdate(ORMModel):
    creditoFecha: date | None = None
    creditoEntrada: float | None = None
    creditoSaldo: float | None = None
    creditoTotal: float | None = None
    Cliente_idCliente: int | None = None
    Usuario_idUsuario: int | None = None
    creditoEstado: int | None = None


class CreditoRead(CreditoBase):
    idCreditoCliente: int
