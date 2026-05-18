from .common import ORMModel


class AlmacenBase(ORMModel):
    almNombre: str
    almPercha: str
    almEstante: str


class AlmacenCreate(AlmacenBase):
    pass


class AlmacenUpdate(ORMModel):
    almNombre: str | None = None
    almPercha: str | None = None
    almEstante: str | None = None


class AlmacenRead(AlmacenBase):
    idAlmacen: int


class CategoriaBase(ORMModel):
    catNombre: str


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(ORMModel):
    catNombre: str | None = None


class CategoriaRead(CategoriaBase):
    idCategoria: int


class MarcaBase(ORMModel):
    marNombre: str


class MarcaCreate(MarcaBase):
    pass


class MarcaUpdate(ORMModel):
    marNombre: str | None = None


class MarcaRead(MarcaBase):
    idMarca: int


class ImpuestoBase(ORMModel):
    impNombre: str
    impValor: int


class ImpuestoCreate(ImpuestoBase):
    pass


class ImpuestoUpdate(ORMModel):
    impNombre: str | None = None
    impValor: int | None = None


class ImpuestoRead(ImpuestoBase):
    idImpuesto: int
