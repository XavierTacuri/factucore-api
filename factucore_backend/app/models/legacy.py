from datetime import date

from sqlalchemy import Column, ForeignKey, String
from sqlmodel import Field, Relationship, SQLModel


class Almacen(SQLModel, table=True):
    __tablename__ = "almacen"

    idAlmacen: int | None = Field(default=None, primary_key=True)
    almNombre: str = Field(max_length=35)
    almPercha: str = Field(max_length=25)
    almEstante: str = Field(max_length=25)


class Categoria(SQLModel, table=True):
    __tablename__ = "categoria"

    idCategoria: int | None = Field(default=None, primary_key=True)
    catNombre: str = Field(max_length=45)


class Marca(SQLModel, table=True):
    __tablename__ = "marca"

    idMarca: int | None = Field(default=None, primary_key=True)
    marNombre: str = Field(max_length=35)


class Impuesto(SQLModel, table=True):
    __tablename__ = "impuesto"

    idImpuesto: int | None = Field(default=None, primary_key=True)
    impNombre: str = Field(max_length=20)
    impValor: int


class Cliente(SQLModel, table=True):
    __tablename__ = "cliente"

    idCliente: int | None = Field(default=None, primary_key=True)
    cedula: str = Field(sa_column=Column(String(13), unique=True, nullable=False))
    cli_nombre: str = Field(max_length=80)
    cli_apellido: str = Field(max_length=80)
    cli_telefono: str = Field(max_length=25)
    cli_direccion: str = Field(max_length=55)
    cli_descripcion: str = Field(max_length=45)
    cli_mail: str = Field(max_length=45)

    facturas: list["Factura"] = Relationship(back_populates="cliente")
    ordenes_trabajo: list["OrdenTrabajo"] = Relationship(back_populates="cliente")


class Rol(SQLModel, table=True):
    __tablename__ = "rol"

    idRol: int | None = Field(default=None, primary_key=True)
    rolNombre: str = Field(sa_column=Column(String(30), unique=True, nullable=False))
    rolDescripcion: str | None = Field(default=None, max_length=100)
    rolEstado: bool = True

    usuarios: list["Usuario"] = Relationship(back_populates="rol")


class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"

    idUsuario: int | None = Field(default=None, primary_key=True)
    userCedula: str = Field(max_length=13)
    userNombre: str = Field(max_length=35)
    userApellido: str = Field(max_length=40)
    userFono: str = Field(max_length=20)
    userDireccion: str = Field(max_length=45)
    userFecha: str = Field(max_length=12)
    userMail: str = Field(max_length=45)
    userUsuario: str = Field(max_length=15)
    userClave: str = Field(max_length=255)
    userEstado: bool | None = None
    userPrincipal: bool | None = None
    idRol: int = Field(foreign_key="rol.idRol")

    rol: Rol = Relationship(back_populates="usuarios")
    facturas: list["Factura"] = Relationship(back_populates="usuario")
    ordenes_trabajo: list["OrdenTrabajo"] = Relationship(back_populates="usuario")


class Articulo(SQLModel, table=True):
    __tablename__ = "articulo"

    idArticulo: int | None = Field(default=None, primary_key=True)
    artCodigo: str = Field(max_length=35)
    artDescripcion: str = Field(max_length=50)
    artCosto: float
    artPVP: float
    artPVMayorista: float
    artPVMinimo: float
    artSerie: int
    artStockMin: int
    artEstado: int
    categoria_idCategoria: int = Field(foreign_key="categoria.idCategoria")
    marca_idMarca: int = Field(foreign_key="marca.idMarca")
    impuesto_idImpuesto: int = Field(foreign_key="impuesto.idImpuesto")


class Inventario(SQLModel, table=True):
    __tablename__ = "inventario"

    idInventario: int | None = Field(default=None, primary_key=True)
    invCantidad: int
    invStock: int
    invEstado: int
    almacen_idAlmacen: int = Field(foreign_key="almacen.idAlmacen")
    articulo_idArticulo: int = Field(foreign_key="articulo.idArticulo")


class Credito(SQLModel, table=True):
    __tablename__ = "credito"

    idCreditoCliente: int | None = Field(default=None, primary_key=True)
    creditoFecha: date
    creditoEntrada: float
    creditoSaldo: float
    creditoTotal: float
    Cliente_idCliente: int = Field(foreign_key="cliente.idCliente")
    Usuario_idUsuario: int = Field(foreign_key="usuario.idUsuario")
    creditoEstado: int


class Factura(SQLModel, table=True):
    __tablename__ = "factura"

    idFactura: int | None = Field(default=None, primary_key=True)
    subtotal14: float
    subtotal0: float
    descuento: float
    subtotalSinImp: float
    iva0: float
    iva: float
    total: float
    fecha: date
    descripsion: str = Field(max_length=45)
    plazo: int
    fEntrada: float
    fSaldo: float
    utilidad: float
    cliente_idCliente: int = Field(
        sa_column=Column(ForeignKey("cliente.idCliente"), nullable=False)
    )
    credito_idCreditoCliente: int = Field(foreign_key="credito.idCreditoCliente")
    usuario_idUsuario: int = Field(
        sa_column=Column(ForeignKey("usuario.idUsuario"), nullable=False)
    )
    secuencia: int
    ptoEmicion: int
    establecimiento: int
    comprobante: int
    facEstado: int
    tipoCredito: int
    facImpuesto: int
    fac_claveacceso: str = Field(max_length=50)
    fac_sriestado: str = Field(max_length=25)
    fac_enviocliente: int

    cliente: Cliente | None = Relationship(back_populates="facturas")
    usuario: Usuario | None = Relationship(back_populates="facturas")
    detalles: list["Detalle"] = Relationship(back_populates="factura")


class Detalle(SQLModel, table=True):
    __tablename__ = "detalle"

    idDetalle: int | None = Field(default=None, primary_key=True)
    cantidad: int
    codPrincipal: str = Field(max_length=35)
    descripcion: str = Field(max_length=55)
    valorUnitario: float
    det_descuento: float
    valorTotal: float
    factura_idFactura: int = Field(
        sa_column=Column(ForeignKey("factura.idFactura"), nullable=False)
    )
    # TODO: El SQL legacy no declara FK para estas columnas; validar datos huerfanos antes.
    inventario_idInventario: int
    idVenta: int
    idOrdenTrabajo: int
    detValorConImpuesto: float
    idTalla: int
    idSerie: int

    factura: Factura | None = Relationship(back_populates="detalles")


class Deposito(SQLModel, table=True):
    __tablename__ = "deposito"

    idDeposito: int | None = Field(default=None, primary_key=True)
    dFecha: date
    valor: float
    saldo: float
    Deposito: float
    concepto: str = Field(max_length=10)
    comprobante: int
    descripcion: str = Field(max_length=45)
    credito_idCreditoCliente: int = Field(foreign_key="credito.idCreditoCliente")
    usuario_idUsuario: int = Field(foreign_key="usuario.idUsuario")
    idFactura: int
    tipoPago: int


class OrdenTrabajo(SQLModel, table=True):
    __tablename__ = "ordentrabajo"

    idOrden: int | None = Field(default=None, primary_key=True)
    doNumero: int
    doFechaIngreso: date
    doFechaSalida: date
    doTotal: float
    doSaldo: float
    doAbono: float
    cliente_idCliente: int = Field(
        sa_column=Column(ForeignKey("cliente.idCliente"), nullable=False)
    )
    usuario_idUsuario: int = Field(
        sa_column=Column(ForeignKey("usuario.idUsuario"), nullable=False)
    )
    doEstado: int

    cliente: Cliente | None = Relationship(back_populates="ordenes_trabajo")
    usuario: Usuario | None = Relationship(back_populates="ordenes_trabajo")
    detalles: list["DetalleOrden"] = Relationship(back_populates="orden")


class DetalleOrden(SQLModel, table=True):
    __tablename__ = "detalleorden"

    idDetalleOrden: int | None = Field(default=None, primary_key=True)
    otMarca: str = Field(max_length=25)
    otModelo: str = Field(max_length=25)
    otSerie: str = Field(max_length=20)
    otDanio: str = Field(max_length=50)
    otObservacion: str = Field(max_length=45)
    otEstado: str = Field(max_length=45)
    otEstadoReparacion: str = Field(max_length=15)
    otTecnico: str = Field(max_length=35)
    otValor: float
    otAbono: float
    ordentrabajo_idOrden: int = Field(
        sa_column=Column(ForeignKey("ordentrabajo.idOrden"), nullable=False)
    )
    otFacturado: int
    otNunEntrega: int
    impuesto_idImpuesto: int

    orden: OrdenTrabajo | None = Relationship(back_populates="detalles")


class Proforma(SQLModel, table=True):
    __tablename__ = "proforma"

    idProforma: int | None = Field(default=None, primary_key=True)
    pro_subtotal14: float
    pro_subtotal0: float
    pro_descuento: float
    pro_subtotalSinImp: float
    pro_iva0: float
    pro_iva: float
    pro_total: float
    pro_fecha: date
    pro_descripsion: str = Field(max_length=45)
    pro_plazo: int
    cliente_idCliente: int = Field(foreign_key="cliente.idCliente")
    usuario_idUsuario: int = Field(foreign_key="usuario.idUsuario")
    comprobante: int
    pro_Estado: int
    pro_tipoCredito: int
    pro_Impuesto: int
    pro_opiva: int


class DetalleProforma(SQLModel, table=True):
    __tablename__ = "detalleproforma"

    idDetalleProforma: int | None = Field(default=None, primary_key=True)
    detpro_cantidad: int
    detpro_valorUnitario: float
    detpro_det_descuento: float
    detpro_valorTotal: float
    proforma_idProforma: int = Field(foreign_key="proforma.idProforma")
    inventario_idInventario: int
    idVenta: int
    idOrdenTrabajo: int
    detpro_detValorConImpuesto: float
    idTalla: int
    idSerie: int


class Proveedor(SQLModel, table=True):
    __tablename__ = "proveedor"

    idProveedor: int | None = Field(default=None, primary_key=True)
    proRuc: str = Field(max_length=13)
    proNombre: str = Field(max_length=55)
    proCiudad: str = Field(max_length=35)
    proDireccion: str = Field(max_length=85)
    proTelefono: str = Field(max_length=32)
    proCelular: str = Field(max_length=21)
    proMail: str = Field(max_length=35)
    proBanco1: str = Field(max_length=35)
    proBanco2: str = Field(max_length=35)
    proCuenta1: str = Field(max_length=11)
    proCuenta2: str = Field(max_length=11)
    proTipoCuenta1: int
    proTipoCuenta2: int
    proProducto: str = Field(max_length=60)
    proEstado: bool
    proColor: str = Field(max_length=25)


class FacturaProveedor(SQLModel, table=True):
    __tablename__ = "facturasproveedor"

    idFacturaProveedor: int | None = Field(default=None, primary_key=True)
    fpFactura: str = Field(max_length=25)
    fpSubtotal: float
    fpSubtotal0: float
    fpIva: float
    fpTotal: float
    fpCredito: str = Field(max_length=11)
    fpFecha: date
    fpPlazo: str = Field(max_length=10)
    Usuario_idUsuario: int = Field(foreign_key="usuario.idUsuario")
    proveedor_idProveedor: int = Field(foreign_key="proveedor.idProveedor")
    fpSaldo: float
    fpAbono: float


class DetalleCompra(SQLModel, table=True):
    __tablename__ = "detallecompras"

    idCompras: int | None = Field(default=None, primary_key=True)
    com_cantidad: int
    com_valorunitario: float
    com_valortotal: float
    facturasProveedor_idFacturaProveedor: int = Field(
        foreign_key="facturasproveedor.idFacturaProveedor"
    )
    # TODO: El SQL legacy no declara FK para estas columnas; validar datos huerfanos antes.
    idInventario: int
    Articulo_idArticulo: int


class DescuentoCliente(SQLModel, table=True):
    __tablename__ = "descuentocliente"

    idDescuento: int | None = Field(default=None, primary_key=True)
    des_tipo: str = Field(max_length=25)
    des_porcentaje: float
    des_condicion: str = Field(max_length=150)
    categoria_idCategoria: int = Field(foreign_key="categoria.idCategoria")


class AsignarDescuento(SQLModel, table=True):
    __tablename__ = "asignardescuento"

    idAsignar: int | None = Field(default=None, primary_key=True)
    cliente_idCliente: int = Field(foreign_key="cliente.idCliente")
    descuento_idDescuento: int = Field(foreign_key="descuentocliente.idDescuento")


class Talla(SQLModel, table=True):
    __tablename__ = "talla"

    idTalla: int | None = Field(default=None, primary_key=True)
    tallaCantidad: int
    talTalla: str = Field(max_length=25)
    articulo_idArticulo: int = Field(foreign_key="articulo.idArticulo")
    inventario_idInventario: int = Field(foreign_key="inventario.idInventario")
    tallaCodigo: str = Field(max_length=35)


class Serie(SQLModel, table=True):
    __tablename__ = "serie"

    idSerie: int | None = Field(default=None, primary_key=True)
    serieNun1: str = Field(max_length=40)
    serieNun2: str = Field(max_length=40)
    serieStock: int
    articulo_idArticulo: int = Field(foreign_key="articulo.idArticulo")
    inventario_idInventario: int = Field(foreign_key="inventario.idInventario")


class Kardex(SQLModel, table=True):
    __tablename__ = "kardex"

    idKardex: int | None = Field(default=None, primary_key=True)
    kar_tipo: int
    kar_fecha: date
    kar_hora: str = Field(max_length=8)
    kar_motivo: str = Field(max_length=90)
    kar_cant_ingreso: float
    kar_cant_egreso: float
    kar_saldo_anterior: float
    kar_saldo_actual: float
    kar_observacion: str = Field(max_length=90)
    idInvOrigen: int
    kar_almacen_origen: str = Field(max_length=30)
    ker_almacen_destino: str = Field(max_length=35)
    idArticulo: int
    idUsuario: int


class VentaDelDia(SQLModel, table=True):
    __tablename__ = "ventadeldia"

    idVenta: int | None = Field(default=None, primary_key=True)
    ven_Fecha: date
    ven_Hora: str = Field(max_length=10)
    ven_Codigo: str = Field(max_length=30)
    ven_Cantidad: int
    ven_Descripcion: str = Field(max_length=75)
    ven_Costo: float
    ven_Utilidad: float
    ven_Estado: int
    inventario_idInventario: int = Field(foreign_key="inventario.idInventario")
    usuario_idUsuario: int = Field(foreign_key="usuario.idUsuario")
    idTalla: int
    idSerie: int
    impuesto: int


class IngresoCaja(SQLModel, table=True):
    __tablename__ = "ingresocaja"

    idIngreso: int | None = Field(default=None, primary_key=True)
    cajaIngreso: float
    cajaEgreso: float
    cajaConcepto: str = Field(max_length=100)
    cajaFecha: date
    cajaHora: str = Field(max_length=8)
    usuario_idUsuario: int = Field(foreign_key="usuario.idUsuario")
    idDeposito: int
    idFactura: int
    idVenta: int
    idOrden: int


class Pedido(SQLModel, table=True):
    __tablename__ = "pedido"

    idPedido: int = Field(primary_key=True)
    pedNombre: str = Field(max_length=45)
    pedFecha: date
    pedObservacion: str = Field(max_length=65)
    usuario_idUsuario: int = Field(foreign_key="usuario.idUsuario")


class DetallePedido(SQLModel, table=True):
    __tablename__ = "detallepedido"

    idDetallePedido: int = Field(primary_key=True)
    pedCantidad: int
    pedDescripcion: str = Field(max_length=100)
    pedido_idPedido: int = Field(foreign_key="pedido.idPedido")


class Nota(SQLModel, table=True):
    __tablename__ = "nota"

    idNota: int | None = Field(default=None, primary_key=True)
    not_fecha: date
    not_cliente: str = Field(max_length=55)
    not_descripcion: str = Field(max_length=150)
    cliente_idCliente: int


class GuardarVenta(SQLModel, table=True):
    __tablename__ = "guardarventa"

    idGuardarVenta: int | None = Field(default=None, primary_key=True)
    factura_idFactura: int = Field(foreign_key="factura.idFactura")
    gvFecha: date
    gvNombre: str = Field(max_length=50)


class PagosProveedor(SQLModel, table=True):
    __tablename__ = "pagosproveedor"

    idPagosproveedor: int | None = Field(default=None, primary_key=True)
    pp_estado: bool
    pp_factura: str = Field(max_length=50)
    pp_fechaemision: date
    pp_Numerorecibo: str = Field(max_length=10)
    pp_formapago: str = Field(max_length=50)
    pp_cheque: str = Field(max_length=15)
    pp_valorcheque: float
    pp_banco: str = Field(max_length=50)
    pp_destino: str = Field(max_length=50)
    pp_fechapago: date
    pp_valor: float
    pp_saldo: float
    pp_fechaqpago: date
    pp_observacion: str = Field(max_length=75)
    usuario_idUsuario: int = Field(foreign_key="usuario.idUsuario")
    # TODO: Nombre ambiguo en SQL legacy: columna proveedor_idFactura con indice factura_idFactura.
    proveedor_idFactura: int


class ConfigCorreo(SQLModel, table=True):
    __tablename__ = "configcorreo"

    idConfigCorreo: int | None = Field(default=None, primary_key=True)
    correoEnviador: str = Field(max_length=50)
    claveAplicacion: str = Field(max_length=25)
    correoReceptor1: str = Field(max_length=50)
    correoReceptor2: str = Field(max_length=50)
    respaldo: int
    correo: int
