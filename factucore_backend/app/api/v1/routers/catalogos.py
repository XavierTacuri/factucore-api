from fastapi import APIRouter, status

from app.api.deps import SessionDep
from app.models.legacy import Almacen, Categoria, Impuesto, Marca
from app.schemas.catalogos import (
    AlmacenCreate,
    AlmacenRead,
    AlmacenUpdate,
    CategoriaCreate,
    CategoriaRead,
    CategoriaUpdate,
    ImpuestoCreate,
    ImpuestoRead,
    ImpuestoUpdate,
    MarcaCreate,
    MarcaRead,
    MarcaUpdate,
)
from app.services import CRUDService

router = APIRouter()

almacenes = CRUDService[Almacen, AlmacenCreate, AlmacenUpdate](Almacen, "idAlmacen")
categorias = CRUDService[Categoria, CategoriaCreate, CategoriaUpdate](Categoria, "idCategoria")
marcas = CRUDService[Marca, MarcaCreate, MarcaUpdate](Marca, "idMarca")
impuestos = CRUDService[Impuesto, ImpuestoCreate, ImpuestoUpdate](Impuesto, "idImpuesto")


@router.get("/almacenes", response_model=list[AlmacenRead])
async def list_almacenes(session: SessionDep, offset: int = 0, limit: int = 50):
    return await almacenes.list(session, offset, limit)


@router.post("/almacenes", response_model=AlmacenRead, status_code=status.HTTP_201_CREATED)
async def create_almacen(payload: AlmacenCreate, session: SessionDep):
    return await almacenes.create(session, payload)


@router.get("/categorias", response_model=list[CategoriaRead])
async def list_categorias(session: SessionDep, offset: int = 0, limit: int = 50):
    return await categorias.list(session, offset, limit)


@router.post("/categorias", response_model=CategoriaRead, status_code=status.HTTP_201_CREATED)
async def create_categoria(payload: CategoriaCreate, session: SessionDep):
    return await categorias.create(session, payload)


@router.get("/marcas", response_model=list[MarcaRead])
async def list_marcas(session: SessionDep, offset: int = 0, limit: int = 50):
    return await marcas.list(session, offset, limit)


@router.post("/marcas", response_model=MarcaRead, status_code=status.HTTP_201_CREATED)
async def create_marca(payload: MarcaCreate, session: SessionDep):
    return await marcas.create(session, payload)


@router.get("/impuestos", response_model=list[ImpuestoRead])
async def list_impuestos(session: SessionDep, offset: int = 0, limit: int = 50):
    return await impuestos.list(session, offset, limit)


@router.post("/impuestos", response_model=ImpuestoRead, status_code=status.HTTP_201_CREATED)
async def create_impuesto(payload: ImpuestoCreate, session: SessionDep):
    return await impuestos.create(session, payload)
