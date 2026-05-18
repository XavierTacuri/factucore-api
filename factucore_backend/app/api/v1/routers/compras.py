from fastapi import APIRouter, status

from app.api.deps import SessionDep
from app.models.legacy import FacturaProveedor, Proveedor
from app.schemas.compras import (
    FacturaProveedorCreate,
    FacturaProveedorRead,
    FacturaProveedorUpdate,
    ProveedorCreate,
    ProveedorRead,
    ProveedorUpdate,
)
from app.services import CRUDService

router = APIRouter()

proveedores = CRUDService[Proveedor, ProveedorCreate, ProveedorUpdate](Proveedor, "idProveedor")
facturas_proveedor = CRUDService[
    FacturaProveedor, FacturaProveedorCreate, FacturaProveedorUpdate
](FacturaProveedor, "idFacturaProveedor")


@router.get("/proveedores", response_model=list[ProveedorRead])
async def list_proveedores(session: SessionDep, offset: int = 0, limit: int = 50):
    return await proveedores.list(session, offset, limit)


@router.post("/proveedores", response_model=ProveedorRead, status_code=status.HTTP_201_CREATED)
async def create_proveedor(payload: ProveedorCreate, session: SessionDep):
    return await proveedores.create(session, payload)


@router.get("/proveedores/{proveedor_id}", response_model=ProveedorRead)
async def get_proveedor(proveedor_id: int, session: SessionDep):
    return await proveedores.get(session, proveedor_id)


@router.patch("/proveedores/{proveedor_id}", response_model=ProveedorRead)
async def update_proveedor(proveedor_id: int, payload: ProveedorUpdate, session: SessionDep):
    return await proveedores.update(session, proveedor_id, payload)


@router.get("/facturas-proveedor", response_model=list[FacturaProveedorRead])
async def list_facturas_proveedor(session: SessionDep, offset: int = 0, limit: int = 50):
    return await facturas_proveedor.list(session, offset, limit)


@router.post(
    "/facturas-proveedor",
    response_model=FacturaProveedorRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_factura_proveedor(payload: FacturaProveedorCreate, session: SessionDep):
    return await facturas_proveedor.create(session, payload)
