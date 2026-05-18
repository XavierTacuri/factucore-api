from fastapi import APIRouter

from .routers import (
    catalogos,
    compras,
    facturas,
    health,
    ordenes,
    personas,
    productos,
    proformas,
)

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(personas.router, prefix="/personas", tags=["personas"])
api_router.include_router(catalogos.router, prefix="/catalogos", tags=["catalogos"])
api_router.include_router(productos.router, prefix="/productos", tags=["productos"])
api_router.include_router(facturas.router, prefix="/facturas", tags=["facturas"])
api_router.include_router(compras.router, prefix="/compras", tags=["compras"])
api_router.include_router(proformas.router, prefix="/proformas", tags=["proformas"])
api_router.include_router(ordenes.router, prefix="/ordenes-trabajo", tags=["ordenes-trabajo"])
