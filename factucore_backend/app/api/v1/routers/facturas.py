from fastapi import APIRouter, status

from app.api.deps import SessionDep
from app.models.legacy import Credito, Detalle, Factura
from app.schemas.ventas import (
    CreditoCreate,
    CreditoRead,
    CreditoUpdate,
    DetalleCreate,
    DetalleRead,
    DetalleUpdate,
    FacturaCreate,
    FacturaRead,
    FacturaUpdate,
)
from app.services import CRUDService

router = APIRouter()

facturas = CRUDService[Factura, FacturaCreate, FacturaUpdate](Factura, "idFactura")
detalles = CRUDService[Detalle, DetalleCreate, DetalleUpdate](Detalle, "idDetalle")
creditos = CRUDService[Credito, CreditoCreate, CreditoUpdate](Credito, "idCreditoCliente")


@router.get("", response_model=list[FacturaRead])
async def list_facturas(session: SessionDep, offset: int = 0, limit: int = 50):
    return await facturas.list(session, offset, limit)


@router.post("", response_model=FacturaRead, status_code=status.HTTP_201_CREATED)
async def create_factura(payload: FacturaCreate, session: SessionDep):
    return await facturas.create(session, payload)


@router.get("/detalles", response_model=list[DetalleRead])
async def list_detalles(session: SessionDep, offset: int = 0, limit: int = 50):
    return await detalles.list(session, offset, limit)


@router.post("/detalles", response_model=DetalleRead, status_code=status.HTTP_201_CREATED)
async def create_detalle(payload: DetalleCreate, session: SessionDep):
    return await detalles.create(session, payload)


@router.get("/creditos", response_model=list[CreditoRead])
async def list_creditos(session: SessionDep, offset: int = 0, limit: int = 50):
    return await creditos.list(session, offset, limit)


@router.post("/creditos", response_model=CreditoRead, status_code=status.HTTP_201_CREATED)
async def create_credito(payload: CreditoCreate, session: SessionDep):
    return await creditos.create(session, payload)


@router.get("/{factura_id}", response_model=FacturaRead)
async def get_factura(factura_id: int, session: SessionDep):
    return await facturas.get(session, factura_id)


@router.patch("/{factura_id}", response_model=FacturaRead)
async def update_factura(factura_id: int, payload: FacturaUpdate, session: SessionDep):
    return await facturas.update(session, factura_id, payload)
