from fastapi import APIRouter, status

from app.api.deps import SessionDep
from app.models.legacy import Articulo, Inventario
from app.schemas.productos import (
    ArticuloCreate,
    ArticuloRead,
    ArticuloUpdate,
    InventarioCreate,
    InventarioRead,
    InventarioUpdate,
)
from app.services import CRUDService

router = APIRouter()

articulos = CRUDService[Articulo, ArticuloCreate, ArticuloUpdate](Articulo, "idArticulo")
inventario = CRUDService[Inventario, InventarioCreate, InventarioUpdate](
    Inventario, "idInventario"
)


@router.get("/articulos", response_model=list[ArticuloRead])
async def list_articulos(session: SessionDep, offset: int = 0, limit: int = 50):
    return await articulos.list(session, offset, limit)


@router.post("/articulos", response_model=ArticuloRead, status_code=status.HTTP_201_CREATED)
async def create_articulo(payload: ArticuloCreate, session: SessionDep):
    return await articulos.create(session, payload)


@router.get("/articulos/{articulo_id}", response_model=ArticuloRead)
async def get_articulo(articulo_id: int, session: SessionDep):
    return await articulos.get(session, articulo_id)


@router.patch("/articulos/{articulo_id}", response_model=ArticuloRead)
async def update_articulo(articulo_id: int, payload: ArticuloUpdate, session: SessionDep):
    return await articulos.update(session, articulo_id, payload)


@router.get("/inventario", response_model=list[InventarioRead])
async def list_inventario(session: SessionDep, offset: int = 0, limit: int = 50):
    return await inventario.list(session, offset, limit)


@router.post("/inventario", response_model=InventarioRead, status_code=status.HTTP_201_CREATED)
async def create_inventario(payload: InventarioCreate, session: SessionDep):
    return await inventario.create(session, payload)
