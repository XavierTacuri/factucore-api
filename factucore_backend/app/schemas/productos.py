from .common import ORMModel


class ArticuloBase(ORMModel):
    artCodigo: str
    artDescripcion: str
    artCosto: float
    artPVP: float
    artPVMayorista: float
    artPVMinimo: float
    artSerie: int = 0
    artStockMin: int = 0
    artEstado: int = 1
    categoria_idCategoria: int
    marca_idMarca: int
    impuesto_idImpuesto: int


class ArticuloCreate(ArticuloBase):
    pass


class ArticuloUpdate(ORMModel):
    artCodigo: str | None = None
    artDescripcion: str | None = None
    artCosto: float | None = None
    artPVP: float | None = None
    artPVMayorista: float | None = None
    artPVMinimo: float | None = None
    artSerie: int | None = None
    artStockMin: int | None = None
    artEstado: int | None = None
    categoria_idCategoria: int | None = None
    marca_idMarca: int | None = None
    impuesto_idImpuesto: int | None = None


class ArticuloRead(ArticuloBase):
    idArticulo: int


class InventarioBase(ORMModel):
    invCantidad: int
    invStock: int
    invEstado: int = 1
    almacen_idAlmacen: int
    articulo_idArticulo: int


class InventarioCreate(InventarioBase):
    pass


class InventarioUpdate(ORMModel):
    invCantidad: int | None = None
    invStock: int | None = None
    invEstado: int | None = None
    almacen_idAlmacen: int | None = None
    articulo_idArticulo: int | None = None


class InventarioRead(InventarioBase):
    idInventario: int
