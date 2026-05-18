from fastapi import APIRouter, status

from app.api.deps import SessionDep
from app.models.legacy import OrdenTrabajo
from app.schemas.ordenes import OrdenTrabajoCreate, OrdenTrabajoRead, OrdenTrabajoUpdate
from app.services import CRUDService

router = APIRouter()
ordenes = CRUDService[OrdenTrabajo, OrdenTrabajoCreate, OrdenTrabajoUpdate](
    OrdenTrabajo, "idOrden"
)


@router.get("", response_model=list[OrdenTrabajoRead])
async def list_ordenes(session: SessionDep, offset: int = 0, limit: int = 50):
    return await ordenes.list(session, offset, limit)


@router.post("", response_model=OrdenTrabajoRead, status_code=status.HTTP_201_CREATED)
async def create_orden(payload: OrdenTrabajoCreate, session: SessionDep):
    return await ordenes.create(session, payload)


@router.get("/{orden_id}", response_model=OrdenTrabajoRead)
async def get_orden(orden_id: int, session: SessionDep):
    return await ordenes.get(session, orden_id)


@router.patch("/{orden_id}", response_model=OrdenTrabajoRead)
async def update_orden(orden_id: int, payload: OrdenTrabajoUpdate, session: SessionDep):
    return await ordenes.update(session, orden_id, payload)
